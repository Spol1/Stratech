from app import db

class Player(db.Model):
    #keys
    id = db.Column(db.String(5), primary_key = True)
    team = db.Column(db.Integer, nullable = False)
    year = db.Column(db.String(4), nullable = False)
    #Research and Development
    performance = db.Column(db.Integer, nullable = False)
    size = db.Column(db.Integer, nullable = False)
    reliability = db.Column(db.Integer, nullable = False)
    #Marketing
    price = db.Column(db.Integer, nullable = False)
    promo_budget = db.Column(db.Integer, nullable = False)
    sales_budget = db.Column(db.Integer, nullable = False)
    unit_sales_forecast = db.Column(db.Integer, nullable = False)
    #Production
    production_order = db.Column(db.Integer, nullable = False)
    #Finance
    current_debt = db.Column(db.Integer)
    bond_issue = db.Column(db.Integer)
    bond_retire = db.Column(db.Integer)
    #Calculation
    awareness = db.Column(db.Integer)
    accessibility = db.Column(db.Integer)
    favorability = db.Column(db.Integer)
    units_sold = db.Column(db.Integer)
    revenue = db.Column(db.Integer)
    market_share = db.Column(db.Integer)
    #Information
    plant_capacity = db.Column(db.Integer)
    inventory = db.Column(db.Integer)
    stock_out = db.Column(db.Boolean)
    cash = db.Column(db.Integer)
    e_loan = db.Column(db.Integer)    

    def __repr__(self):
        return '<Player %r>' % self.id

class World(db.Model):
    year_id = db.Column(db.String(5), primary_key=True)
    
    promo_expense = db.Column(db.Integer, nullable = False)
    sales_expense = db.Column(db.Integer, nullable = False)
    performance = db.Column(db.Integer, nullable = False)
    size = db.Column(db.Integer, nullable = False)
    reliability = db.Column(db.Integer, nullable = False)
    
    time_to_improve_metric = db.Column(db.Integer, nullable = False)
    tax_rate = db.Column(db.Integer, nullable = False)
    ideal_performance = db.Column(db.Integer, nullable = False)
    
    awareness_bonus = db.Column(db.Integer)
    accessibility_bonus = db.Column(db.Integer)
    
    total_units_sold = db.Column(db.Integer)
    total_favourability = db.Column(db.Integer)
    total_revenue = db.Column(db.Integer)
    
    min_price = db.Column(db.Integer)
    max_price = db.Column(db.Integer)

    def __repr__(self):
        return '<World %r>' % self.id
    
class bonds(db.Model):
    bond_id = db.Column(db.String(5), primary_key=True)

    Player_assigned = db.Column(db.String(5), nullable = False)
    maturity_year = db.Column(db.String(4), nullable = False)
    principal = db.Column(db.Integer, nullable = False)
    rate_of_interest = db.Column(db.Integer, nullable = False)
    
    def __repr__(self):
        return '<bonds %r>' % self.id