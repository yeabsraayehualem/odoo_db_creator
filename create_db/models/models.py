from odoo import models, fields, api
from odoo.service import db
from odoo import exceptions
import odoo
class DBCreatorWizard(models.TransientModel):
    _name = 'db.creator.wizard'
    _description = 'Database Creator Wizard'

    db_name = fields.Char(string="Database Name", required=True)
    admin_email = fields.Char(string="Admin Email", required=True)
    admin_password = fields.Char(string="Admin Password", required=True)

    def create_database(self):
        """Create a new database with the provided name and admin details."""
        db_name = self.db_name
        admin_email = self.admin_email
        admin_password = self.admin_password

        # Check if the database already exists
        if db_name in db.list_dbs():
            raise exceptions.ValidationError("A database with this name already exists.")

        # Create the database
        db.exp_create_database(
            db_name, 
            demo=False, 
            lang='en_US', 
            user_password=admin_password
        )

        # Set up the admin user in the new database
        self._setup_admin_user(db_name, admin_email, admin_password)

    def _setup_admin_user(self, db_name, email, password):
        """Initialize the admin user in the new database."""
        registry = odoo.registry(db_name)
        with registry.cursor() as cr:
            env = api.Environment(cr, odoo.SUPERUSER_ID, {})
            user = env['res.users'].browse(odoo.SUPERUSER_ID)
            user.write({
                'login': 'admin',
                'email': email,
                'password': password
            })
