"""A fluent builder for a three-trait developer profile."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Developer:
    curiosity: str
    empathy: str
    adaptability: str

class DeveloperBuilder:
    def __init__(self):
        self._traits = {}

    def with_curiosity(self, description):
        self._traits["curiosity"] = description.strip()
        return self

    def with_empathy(self, description):
        self._traits["empathy"] = description.strip()
        return self

    def with_adaptability(self, description):
        self._traits["adaptability"] = description.strip()
        return self

    def build(self):
        required = ("curiosity", "empathy", "adaptability")
        if any(not self._traits.get(key) for key in required):
            raise ValueError("All three traits need a description.")
        return Developer(**self._traits)

def main():
    developer = (DeveloperBuilder()
        .with_curiosity("Investigates assumptions and tests unfamiliar ideas.")
        .with_empathy("Considers users and explains feedback respectfully.")
        .with_adaptability("Revises a design when new evidence justifies change.")
        .build())
    print("Building your ideal developer...")
    traits = vars(developer)
    for name, description in traits.items():
        print(f"Trait: {name.title()} - {description}")
    print(f"Total traits included: {len(traits)}")

if __name__ == "__main__":
    main()
