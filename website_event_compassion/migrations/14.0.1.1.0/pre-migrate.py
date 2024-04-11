def migrate(cr, version):
    cr.execute(
        """
        UPDATE ir_model_data
        SET module= 'website_switzerland'
        WHERE module = 'website_event_compassion'
        AND (model IN ('mail.template', 'partner.communication.config',
                       'event.registration.task', 'event.type.mail')
        OR name like 'stage_group_%'
        OR name = 'event_type_group_visit'
        OR model like 'survey.%'
        )
    """
    )
    # Force module install
    cr.execute(
        """
        UPDATE ir_module_module
        SET state = 'to install'
        WHERE name = 'website_switzerland'
    """
    )
