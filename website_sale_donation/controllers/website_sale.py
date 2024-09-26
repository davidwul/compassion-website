from odoo.http import request

from odoo.addons.website_sale.controllers.main import WebsiteSale


class WebsiteSaleDonation(WebsiteSale):
    def _checkout_form_save(self, mode, checkout, all_values):
        # Try to match existing partner if possible
        if mode[0] == "new":
            partner = (
                request.env["res.partner.match"]
                .sudo()
                .match_values_to_partner(checkout, match_create=False)
            )
            if partner:
                return partner[:1].id
        return super()._checkout_form_save(mode, checkout, all_values)
