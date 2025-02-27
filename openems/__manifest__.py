{
    "name": "OpenEMS",
    "summary": "Everything related to OpenEMS (Open Energy Management System)",
    "version": "16.0.1.0.0",
    "author": "OpenEMS Association e.V.",
    "maintainer": "OpenEMS Association e.V.",
    "contributors": [
        "Stefan Feilmeier <stefan.feilmeier@fenecon.de>"
        "Maximilian Lang <maximilian.lang@fenecon.de>"
    ],
    "website": "https://openems.io",
    "license": "AGPL-3",
    "category": "Specific Industry Applications",
    "depends": ["base", "web", "mail", "crm", "resource", "stock", "web_m2x_options", "partner_firstname"],
    "data": [
        "data/ir_config_parameter.xml",
        "data/res_partner_category.xml",
        "security/openems.xml",
        "security/ir.model.access.csv",
        "report/setup_protocol.xml",
        "views/device.xml",
        "views/partner.xml",
        "views/setup_protocol.xml",
        "views/user.xml",
        "views/stock_production_lot_views.xml",
        "mail/openems/alerting_offline.xml",
        "mail/openems/alerting_sum_state.xml",
        "mail/openems/setup_protocol_customer.xml",
        "mail/openems/setup_protocol_installer.xml",
        "mail/openems/user_registration.xml",
    ],
    "demo": ["data/demo.xml"],
    "js": [],
    "css": [],
    "qweb": [],
    "images": [],
    "test": [],
    "installable": True,
    "application": True,
}
