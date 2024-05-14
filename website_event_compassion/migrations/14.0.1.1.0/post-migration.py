from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    env.cr.execute(
        """
            UPDATE event_type
            SET compassion_event_type = 'tour'
            WHERE compassion_event_type = 'group_visit'
        """
    )
    # Publish donation products
    env["event.event"].mapped("donation_product_id.product_tmpl_id").write(
        {"is_published": True}
    )
