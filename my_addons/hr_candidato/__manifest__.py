# -*- coding: utf-8 -*-
{
    'name': "hr_candidato",

    'summary': "Esta funcionalidad pasa por varios estados durante su ejecución, ya que el candidato debe pasar por cada una de las etapas del proceso de selección, como son: entrevista preliminar, entrevista de conocimientos, comprobación de las aptitudes psicológicas, comprobación de las actitudes físicas, verificaciones sociolaborales, análisis en comisión de expertos, análisis en consejo de dirección e informe de resultados.",

    'description': """
        Long description of module's purpose
    """,

    'author': "Glezvidal",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Proceso de Selección',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr_recruitment','website_slides','report_xlsx'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/hr_segurity_recruitment.xml',
        'security/segurity_hr_nomengladores.xml',
        'security/segurity_hr_modelo.xml',
        'wizard/hr_w_mouth_report.xml',
        'wizard/hr_w_stage_report.xml',
        'wizard/hr_w_course_report.xml',
        'wizard/hr_w_year_report.xml',
        'wizard/hr_w_job_report.xml',
        'report/hr_mouth_doc.xml',
        'report/hr_job_xlsx.xml',
        'report/hr_stage_pdf.xml',
        'report/hr_course_pdf.xml',
        'report/hr_year_pdf.xml',
        'views/templates.xml',
        'views/hr_recruitment.xml',
        'views/hr_area.xml',
        'views/templates.xml',
        'views/hr_prempleao.xml',
        'views/hr_searchRe.xml',
        'views/hr_resumen.xml',
        'views/hr_psico.xml',
        'views/hr_evalua.xml',
        'views/hr_company.xml',
        'views/hr_ueb.xml',
        'views/hr_n_area.xml',
        'views/hr_job.xml',
        'views/hr_slide.xml',
        'views/hr_aspect.xml',
        'views/hr_stage.xml',
        'views/hr_menu.xml',

    ],
    # only loaded in demonstration mode
    'application': True,
    'installable': True,
}
