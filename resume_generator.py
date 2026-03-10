class Resume:
    def __init__(self):
        self.name = ""
        self.email = ""
        self.phone = ""
        self.skills = []
        self.education = []
        self.experience = []

    def set_personal(self):
        self.name = input("Enter name: ")
        self.email = input("Enter email: ")
        self.phone = input("Enter phone: ")

    def add_skills(self):
        while True:
            skill = input("Enter skill (or 's' to stop): ")
            if skill.lower() == 's':
                break
            self.skills.append(skill)

    def add_education(self):
        while True:
            edu = input("Enter education (or 's' to stop): ")
            if edu.lower() == 's':
                break
            self.education.append(edu)

    def add_experience(self):
        while True:
            exp = input("Enter experience (or 's' to stop): ")
            if exp.lower() == 's':
                break
            self.experience.append(exp)

    def generate_resume(self):
        print("\n===== RESUME =====")
        print("Name:", self.name) 
        print("Email:", self.email)
        print("Phone:", self.phone)

        print("\nSkills:")
        for s in self.skills:
            print("-", s)

        print("\nEducation:")
        for e in self.education:
            print("-", e)

        print("\nExperience:")
        for ex in self.experience:
            print("-", ex)


def main():
    r = Resume()

    r.set_personal()
    r.add_skills()
    r.add_education()
    r.add_experience()

    r.generate_resume()


main()