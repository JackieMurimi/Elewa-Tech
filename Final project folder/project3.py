# a guide on how to hire nannies
class Nanny:
    def __init__(self, name, experience, monthly_rate):
        self.name = name
        self.experience = experience
        self.monthly_rate = monthly_rate

    def display_info(self):
        return f"Nanny: {self.name}\nExperience: {self.experience} years\nMonthly Rate: KES {self.monthly_rate}/month"


class NannyBureau:
    def __init__(self):
        self.nannies = []

    def add_nanny(self, nanny):
        self.nannies.append(nanny)

    def find_nannies_with_experience(self, years_experience):
        qualified_nannies = [nanny for nanny in self.nannies if nanny.experience >= years_experience]
        return qualified_nannies

    def find_affordable_nannies(self, max_rate):
        affordable_nannies = [nanny for nanny in self.nannies if nanny.monthly_rate <= max_rate]
        return affordable_nannies


def main():
    agency = NannyBureau()

    # Adding nannies to the agency
    nanny1 = Nanny("Alice", 3, 15000)
    nanny2 = Nanny("Bob", 5, 8000)
    nanny3 = Nanny("Eve", 2, 9500)

    agency.add_nanny(nanny1)
    agency.add_nanny(nanny2)
    agency.add_nanny(nanny3)

    # Find nannies with at least 3 years of experience
    experienced_nannies = agency.find_nannies_with_experience(3)
    print("Nannies with at least 3 years of experience:")
    for nanny in experienced_nannies:
        print(nanny.display_info())

    # Find affordable nannies with a maximum rate of kes 10,000/month
    affordable_nannies = agency.find_affordable_nannies(15)
    print("\nAffordable nannies with rates up to KES 10,000 per month:")
    for nanny in affordable_nannies:
        print(nanny.display_info())


if __name__ == "__main__":
    main()
