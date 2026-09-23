"""A fluent builder for a three-trait developer profile."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Developer:
    '''Represents an immutable developer profile with curiosity, empathy, and adaptability traits.'''
    curiosity: str
    empathy: str
    adaptability: str

class DeveloperBuilder:
    '''A fluent builder for creating a Developer instance with curiosity, empathy, and adaptability traits.'''
    def __init__(self):
        self._traits = {}

    def with_curiosity(self, description):
        '''Sets the curiosity trait for the developer.'''
        self._traits["curiosity"] = description.strip()
        return self

    def with_empathy(self, description):
        '''Sets the empathy trait for the developer.'''
        self._traits["empathy"] = description.strip()
        return self

    def with_adaptability(self, description):
        '''Sets the adaptability trait for the developer.'''
        self._traits["adaptability"] = description.strip()
        return self

    def build(self):
        '''Constructs and returns a Developer instance after validating all required traits are provided.'''
        required = ("curiosity", "empathy", "adaptability")
        if any(not self._traits.get(key) for key in required):
            raise ValueError("All three traits need a description.")
        return Developer(**self._traits)

def main():
    '''Demonstrates the usage of the DeveloperBuilder to create a Developer instance and print its traits.'''
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
