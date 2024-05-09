def migrate(cr, version):
    cr.execute(
        """
            UPDATE event_type
            SET compassion_event_type = 'tour'
            WHERE compassion_event_type = 'group_visit'
        """
    )
