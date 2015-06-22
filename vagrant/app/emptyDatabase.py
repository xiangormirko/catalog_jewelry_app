#!/usr/bin/env python
#
# emptyDatabase.py -- Run this script to delete all records in the database without dropping
#
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Collection, Base, CollectionItem, User

engine = create_engine('sqlite:///ecommerce.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

print "Fetching and deleting..."
items = session.query(CollectionItem).delete()
print "Items deleted:"
print items
session.commit()
print

print "Fetching and deleting..."
collections = session.query(Collection).delete()
print "Collections deleted:"
print collections
session.commit()
print


print "Fetching and deleting..."
users = session.query(User).delete()
print "Users deleted:"
print users
session.commit()
print





