# -*- coding: utf-8 -*-

{
    # Module Information
    'name': 'Bakhroush Custom - Report',
    'category': 'Fleet Custom',
    'sequence': 1,
    'version': '14.0.1.0.0',
    'license': 'LGPL-3',
    'summary': """Bakhroush Custom - Report""",
    'description': """Bakhroush Custom - Report""",
    # Website
    'author': 'Aneesh.AV',
    # Dependencies
    'depends': ['base','stock','saudi_vat_invoice_print'],
    # Data
    'data': [
        # 'security/ir.model.access.csv',
        'report/delivery_report.xml',
        'report/delivery_dotmatrix_report.xml',
        'report/delivery_concreate_dotmatrix_report.xml',
        'views/stock_picking_view.xml',
        # 'views/res_company_view.xml',
         ],
    'installable': True,
    'application': True,
}
