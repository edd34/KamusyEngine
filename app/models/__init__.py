from app import db

def get_or_add(model, **kwargs):
    """ Get or add a model.
        If a model doesn't exist in DB, it adds it and return the instance.
    """
    instance = db.session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance

    instance = model(**kwargs)
    db.session.add(instance)
    return instance

def get_or_create(model, **kwargs):
    """ Get or create a model.
        If a model doesn't exist in DB, it creates it and return the instance.
    """
    instance = db.session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance

    instance = model(**kwargs)
    db.session.add(instance)
    db.session.commit()
    return instance

def dump_datetime(value):
    """Deserialize datetime object into string form for JSON processing."""
    if value is None:
        return None
    return [value.strftime("%Y-%m-%d"), value.strftime("%H:%M:%S")]
