from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    env.cr.execute(
        """
    UPDATE account_move_line ml
    SET crowdfunding_participant_id = il.crowdfunding_participant_id
    FROM account_invoice_line il
    WHERE ml.old_invoice_line_id = il.id
    AND il.crowdfunding_participant_id IS NOT NULL
    """
    )
    env["product.template"].search([]).recompute_amount()
    products = (
        env["crowdfunding.project"].search([]).mapped("product_id.product_tmpl_id")
    )
    products.write({"website_published": True})
