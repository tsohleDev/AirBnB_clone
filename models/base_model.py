#!/usr/bin/env python3
"""Base model for all models in our object relational mapping."""
import uuid
import datetime

class BaseModel:
    """Base model for all models in our object relational mapping."""
    def __init__(self, *args, **kwargs):
        """Initialize the base model."""
        # If the dictionary is not empty, set the model's attributes
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        # If the dictionary is empty, set the model's attributes
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

    def save(self):
        """Save the model to the database."""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Return a dictionary representation of the model."""
        # Create a dictionary with the model's attributes
        model_dict = self.__dict__.copy()
        # Replace the datetime objects with their string representations
        model_dict["created_at"] = model_dict["created_at"].isoformat()
        model_dict["updated_at"] = model_dict["updated_at"].isoformat()
        # Add the class name to the dictionary
        model_dict["__class__"] = self.__class__.__name__
        return model_dict


    def delete(self):
        """Delete the model from the database."""
        self.delete()

    def __str__(self):
        """Return a string representation of the model."""
        # [<class name>] (<self.id>) <self.__dict__>
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
