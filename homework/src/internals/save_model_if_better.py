from .save_model import save_model
from .compare_model import compare_models


def save_model_if_better(model, x_test, y_test, best_model=None):
    """Save the model if it's better than the best model."""
    best_model = compare_models(model, best_model, x_test, y_test)
    if best_model is model:
        save_model(model)
    return best_model