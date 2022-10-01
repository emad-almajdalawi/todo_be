from mongoengine import Document, StringField, BooleanField, LongField

class ContactGroup(Document):
    _id = LongField(required = True, unique = True)
    title = StringField(max_length = 60, required = True)
    done = BooleanField(required = True, default = False)

    def __unicode__(self):
        return self.title

    def __repr__(self):
        return self.title