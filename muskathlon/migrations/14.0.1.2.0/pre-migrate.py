from openupgradelib import openupgrade

reload_data = [
    "data/event_registration_task.xml",
]


def migrate(cr, version):
    # Associate prod records to XML records
    openupgrade.rename_xmlids(
        cr, [("website_switzerland.criminal_form", "muskathlon.criminal_form")]
    )

    for data in reload_data:
        openupgrade.load_data(cr, "muskathlon", data)
