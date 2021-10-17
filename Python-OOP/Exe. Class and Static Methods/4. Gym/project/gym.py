class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer):
        if not customer in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if not trainer in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if not equipment in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if not plan in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if not subscription in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        # for sub in self.subscription:
        #     if sub.id == subscription_id:
        #         subscription = sub
        #         break
        subscription = [sub for sub in self.subscriptions if sub.id == subscription_id][0]
        customer = [cust for cust in self.customers if cust.id == subscription.customer_id][0]
        trainer = [train for train in self.trainers if train.id == subscription.trainer_id][0]
        plan = [pl for pl in self.plans if pl.trainer_id == trainer.id][0]
        equipment = [eq for eq in self.equipment if eq.id == plan.equipment_id][0]
        return f"{subscription}\n{customer}\n{trainer}\n{equipment}\n{plan}"
