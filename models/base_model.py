#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
from models import storage


"""
Module base_model
Defines class BaseModel for AirBnb clone
"""


class BaseModel:
    """
    Defines all common atrributes/methods for other claseses
    methods:
        __init__
        __str__
        save
        to_dict
    """

    def __init__(self, *args, **kwargs):
        """
        Initialise class BaseModel
        atrributes: id, created-at, updated_at
        """
        if kwargs is not None:
            for key, value in kwargs.items():
                if "created_at" == key:
                    self.created_at = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif "updated_at" == key:
                    self.updated_at = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif "__class__" == key:
                    pass
                else:
                    setattr(self, key, value)
            else:
                self.id = str(uuid4())
                self.created_at = datetime.now()
                self.updated_at = datetime.now()
                storage.new(self)

    def __str__(self):
        """Return string information about base Model"""
        return ("[{}] ({}) {}"
                .format(self.__class__.__name__, self.id, self.__dict__))

    def __repr__(self):
        """
        Returns string representstion
        """
        return (self.__str__())

    def save(self):
        """update updated_at time and save """
        # perform test for this using now to ensure that values
        # created is atleast 3 seconds within range
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        create a dictionary represantion of attributes
        """
        dic = {}

        dic["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if isinstance(value, (datetime)):
                dic[key] = value.isoformat()
            else:
                dic[key] = value
        return dic
