import sys

class NexusAnimaAuditSystem:
    def __init__(self, target_budget_eur=3500000):
        self.target_budget = target_budget_eur
        self.raised_funds = 0.0
        self.disbursed_expenses = []

    def log_investment(self, investor_id: str, amount_eur: float):
        """Logs an incoming investment contribution."""
        if amount_eur <= 0:
            raise ValueError("Investment amount must be positive.")
        self.raised_funds += amount_eur
        progress = (self.raised_funds / self.target_budget) * 100
        print(f"[INVESTMENT RECEIVED] {investor_id}: €{amount_eur:,.2f}")
        print(f" -> Total Capital Raised: €{self.raised_funds:,.2f} / €{self.target_budget:,.2f} ({progress:.2f}%)\n")

    def approve_stage_expense(self, stage_name: str, category: str, amount_eur: float, recipient: str):
        """Validates and executes construction/operational disbursements."""
        if amount_eur > self.raised_funds:
            print(f"[ERROR: REJECTED] Insufficient funds for {stage_name} ({category}). Needed: €{amount_eur:,.2f}")
            return False
        
        self.raised_funds -= amount_eur
        expense_record = {
            "stage": stage_name,
            "category": category,
            "amount": amount_eur,
            "recipient": recipient
        }
        self.disbursed_expenses.append(expense_record)
        print(f"[DISBURSEMENT APPROVED] {stage_name} | {category}")
        print(f" -> Paid €{amount_eur:,.2f} to {recipient}. Remaining Treasury Balance: €{self.raised_funds:,.2f}\n")
        return True


if __name__ == "__main__":
    print("=================================================================")
    print("    HOLISTIC SOLUTIONS - NEXUS ANIMA FINANCIAL AUDIT SIMULATOR   ")
    print("=================================================================\n")

    audit = NexusAnimaAuditSystem(target_budget_eur=3500000)

    # 1. Capital Raising Phase
    audit.log_investment("Institutional Impact Fund A", 1500000)
    audit.log_investment("Web3 $NEXUS Token Sale", 1200000)
    audit.log_investment("Private Healthcare Syndicate", 800000)

    # 2. Executing Stage Expenditures
    audit.approve_stage_expense("Stage 1", "Land Acquisition (5 ha)", 250000, "Land Seller / Notary Escrow")
    audit.approve_stage_expense("Stage 2", "Subterranean Infrastructure & Foundations", 650000, "General Construction Corp")
    audit.approve_stage_expense("Stage 3", "Superstructure & Roofing (Red Shell)", 800000, "Timber & Frame Contractors")
    audit.approve_stage_expense("Stage 4", "MEP, Solar Array & Eco-Finishes", 700000, "Green Systems & Finishing Ltd")
    audit.approve_stage_expense("Stage 5", "Clinical Equipment & Staffing Setup", 350000, "Healthcare Supply Co")

    print("Audit Simulation Completed Successfully. All funds tracked transparently.")
