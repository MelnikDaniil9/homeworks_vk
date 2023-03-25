import enum
import random


class Mood(enum.Enum):
    NEUD = "неуд"
    NORM = "норм"
    OTL = "отл"


class SomeModel:
    def predict(self, message: str) -> float:
        return random.random()


def predict_message_mood(
    message: str,
    model: SomeModel,
    bad_thresholds: float = 0.3,
    good_thresholds: float = 0.8,
) -> str:
    assert message and bad_thresholds < good_thresholds
    rand_mod = model.predict(message)
    if rand_mod < bad_thresholds:
        return Mood.NEUD.value
    if rand_mod > good_thresholds:
        return Mood.OTL.value
    return Mood.NORM.value
