# -*- coding: utf-8 -*-
import openerp
from openerp import api, fields, models, _

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    
    module_account_asset_management = fields.Boolean(string='Account Asset Management',
        help='this Module manages the assets owned by a company. It will keep \n'
              'track of depreciations occurred on those assets. And it allows to create \n'
              'accounting entries from the depreciation lines. \n'
              'The full asset life-cycle is managed (from asset creation to asset removal). \n'
              'Assets can be created manually as well as automatically \n'
              '(via the creation of an accounting entry on the asset account). \n'
              'Excel based reporting is available via the account_asset_management_xls module. \n'
              'The module contains a large number of functional enhancements compared to \n'
              'the standard account_asset module from Odoo. \n'
             '-This installs the module account_asset_management.')
    
    module_account_balance_line = fields.Boolean(string='Account Balance Line',
        help='This module adds a balance total for lines in move line view.\n')

    module_account_chart_update = fields.Boolean(string='Account Chart Update',
        help='This is a pretty useful tool to update Odoo installations after tax reforms \n'
              'on the official charts of accounts, or to apply fixes performed on the chart \n'
              'template. \n'
              'The wizard: \n'
              '* Allows the user to compare a chart and a template showing differences \n'
              '  on accounts, taxes, tax codes and fiscal positions. \n'
              '* It may create the new account, taxes, tax codes and fiscal positions detected \n'
              '  on the template. \n'
              '* It can also update (overwrite) the accounts, taxes, tax codes and fiscal \n'
              ' positions that got modified on the template. \n')

    module_account_check_deposit = fields.Boolean(string='Account Check Deposit',
        help='This module allows you to easily manage check deposits : you can select all \n'
              'the checks you received and create a global deposit for the selected checks. \n'
              'This module supports multi-currency ; each deposit has a currency and all the \n'
              'checks of the deposit must have the same currency (so, if you have checks in \n'
              'EUR and checks in USD, you must create 2 deposits: one in EUR and one in USD). \n'
             '-This installs the module account_check_deposit.')


    module_account_coa_menu = fields.Boolean(string='Account coa Menu',
        help='This module adds menu entries **Chart of Accounts** and all it sub menus under *Invoicing > Configuration*, \n'
              'because this menu entry doesnt exists in the official *account* module of Odoo 12. \n'
              'List of menus :  \n'
              '- Chart of Accounts Templates (account.chart.template) \n'
              '- Account Templates (account.account.template) \n'
              '- Tax Templates (account.tax.template) \n'
              '- Fiscal Positions Templates (account.fiscal.position.template) \n'
              '-This installs the module account_coa_menu .')

    module_account_document_reversal = fields.Boolean(string='Account Document Reversal',
        help='By Odoo standard, when an account document is cancelled, its journal entry will be deleted completely. \n'
              'This module enhance the process, instead of deletion, it will create new reversed journal entry. \n'
              'This will help preserved the accounting history, which is strictly required by some country. \n'
              'Following are documented provide this feature, \n'
              '- Invoice (account.invoice) \n'
              '- Payment (acccont.payment) \n'
              '- Bank Statement (account.bank.statement.line) \n'
            '-This installs the module account_document_reversal .')

    module_account_fiscal_month = fields.Boolean(string='account fiscal month',
        help='This module simply provides a date range type marked as Fiscal month. \n'
             '-This installs the module account_fiscal_month .')

    module_account_fiscal_position_vat_check = fields.Boolean(string='Account Fiscal Position VAT Check',
        help='With this module, when a user tries to validate a customer invoice or refund \n'
              'with a fiscal position that requires VAT, Odoo blocks the validation of the invoice \n'
              'if the customer doesnt have a VAT number in Odoo. \n'
              'In the European Union (EU), when an EU company sends an invoice to \n'
              'another EU company in another country, it can invoice without VAT \n'
              '(most of the time) but the VAT number of the customer must be displayed \n'
              'on the invoice. \n'
             '-This installs the module account_fiscal_position_vat_check .')

    module_account_fiscal_year = fields.Boolean(string='Account Fiscal Year',
        help='This module just adds the menu \n'
              'Invoicing > Configuration > Accounting > Fiscal Years \n'
             '-This installs the module account_fiscal_year .')

    module_account_group_menu = fields.Boolean(string='Account Group Menu',
        help='This module adds menu entries  \n'
              '**Account Groups** and **Account Tax Groups** under *Invoicing > Configuration > Accounting*, \n'
              'because this menu entry doesnt exists in the official *account* module of Odoo 12. \n'
             '-This installs the module account_group_menu .')

    module_account_invoice_constraint_chronology = fields.Boolean(string='Account Invoice Constraint Chronology',
        help='This module helps ensuring the chronology of invoice numbers. \n'
              'It prevents the validation of invoices when: \n'
              '* there are draft invoices with a prior date \n'
              '* there are validated invoices with a later date \n'
             '-This installs the module account_invoice_constraint_chronology .')

    module_account_invoice_currency = fields.Boolean(string='Account Invoice Currency',
        help='This module adds functional fields to show invoices in the company currency: \n'
              'amount untaxed, amount taxed and amount total. \n'
              'These fields are shown in "Other information" tab in invoice form. \n'
             '-This installs the module account_invoice_currency .')

    module_account_lock_date_update = fields.Boolean(string='Account Lock Date Update',
        help='Allow an Account adviser to update locking date without having \n'
             'access to all technical settings. \n'
             '-This installs the module account_lock_date_update .')

    module_account_menu = fields.Boolean(string='Account Menu',
        help='This module adds all missing menu entries for **Account** module. \n'
             '-This installs the module account_menu .')

    module_account_move_budget = fields.Boolean(string='Account Move Budget',
        help='This module allows to define accounting budgets. \n'
              'These budgets can then be used in MIS Builder reports, as an alternate \n'
              'source. \n'
              'The difference between the MIS Builder Budget and this module is that \n'
              'this module defines budgets irrespective of the MIS Builder Template. The \n'
              'budget is thus agnostic of the reporting format. \n'
              'For example, the budgeted data can be used in a general Profit & Loss report \n'
              'and at the same time can be used in a department or project expenses report. \n'
              '-This installs the module account_move_budget .')

    module_account_move_fiscal_year = fields.Boolean(string='Account Move Fiscalyear',
        help='Display the fiscal year on journal entries/items. \n'
             '-This installs the module account_move_fiscal_year .')

    module_account_move_line_purchase_info = fields.Boolean(string='account move line purchase info',
        help='This module will add the purchase order line to journal items. \n'
              'The ultimate goal is to establish the purchase order line as one of the key \n'
              'fields to reconcile the Goods Received Not Invoiced accrual account. \n'
             '-This installs the module account_move_line_purchase_info .')

    module_account_move_line_tax_editable = fields.Boolean(string='Account Move Line Tax Editable',
        help='Allows to edit taxes on account move lines \n'             
             '-This installs the module account_move_line_tax_editable .')


    module_account_netting = fields.Boolean(string='Account Netting',
        help='This module allows to compensate the balance of a receivable account with the \n'
              'balance of a payable account for the same partner, creating a journal item \n'
              'that reflects this operation. \n'
              '**WARNING**: This operation can be forbidden in your country by the accounting \n'
              'regulations, so you should check current laws before using it. For example, in \n'
              'Spain, this is not allowed at first instance, unless you document well the \n'
              'operation from both parties. \n'
             '-This installs the module account_netting .')

    module_account_partner_required = fields.Boolean(string='Account Partner Required',
        help='This module adds an option *Partner policy* on account types. \n'
              'You have the choice between 3 policies: \n'
              '* *optional* (the default policy): partner is optional, \n'
              '* *always*: require a partner, \n'
              '* *never*: forbid a partner. \n'
              'This module is useful to enforce a partner on account move lines on \n'
              'customer and supplier accounts. \n'
             '-This installs the module account_partner_required .')

    module_account_renumber = fields.Boolean(string='Account Renumber',
        help='This module extends the functionality of accounting to allow the accounting \n'
              'manager to renumber account moves by date only for admin. \n'
              'The wizard, which is accesible from the "End of Period" menuitem, \n'
              'lets you select journals, periods, and a starting number. When \n'
              'launched, it renumbers all posted moves that match selected criteria \n'
              '(after ordering them by date). \n'
              'It will recreate the sequence number for each account move \n'
              'using its journal sequence, which means that: \n'
              '- Sequences per journal are supported. \n'
              '- Sequences with prefixes and suffixes based on the move date are also \n'
               ' supported. \n'
             '-This installs the module account_renumber .')

    module_account_spread_cost_revenue = fields.Boolean(string='Account Spread Cost Revenue',
       help='Allows to spread costs or revenues over a customizable periods, to even out cost or invoice spikes. \n'
             '-This installs the module account_spread_cost_revenue .')

    module_account_tag_menu = fields.Boolean(string='Account Ttag Menu',
        help='This module adds a menu entry **Account Tags** under *Invoicing > Configuration > Accounting*, \n'
              'because this menu entry doesnt exists in the official *account* module of Odoo 12. \n'
             '-This installs the module account_tag_menu .')

   
    module_account_type_menu = fields.Boolean(string='Account Type Menu',
        help='This module adds a menu entry **Account Type** under *Invoicing > Configuration > Accounting* \n'
              'because this menu entry doesnt exists in the official *account* module of Odoo 12. \n'
             '-This installs the module account_type_menu .')

    module_base_vat_optional_vies = fields.Boolean(string='Base VAT Optional Vies',
        help='This module extends base_vat module features allowing to know if VIES \n'
              'validation was passed or not. \n'
              'then you can use "VIES validation passed" field in order to show VAT ID with \n'
              'or without country preffix in invoices, for instance. \n'
              '*NOTE*: Although VIES validation is set in your company, this validation \n'
              'will not block VAT ID write (main difference to Odoo standard behavior) if this \n'
              'VAT ID is valid in its country. \n'
             '-This installs the module base_vat_optional_vies .')