from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Category, Item, User

engine = create_engine('sqlite:///grocery.db')
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


# Create dummy user
usertodelete = session.query(User).all()
for u in usertodelete:
   session.delete(u)
session.commit()

User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

# Fruits
itemtodelete = session.query(Item).all()
for itm in itemtodelete:
   session.delete(itm)
session.commit()

cattodelete = session.query(Category).all()
for cat in cattodelete:
   session.delete(cat)
session.commit()


cat1 = Category(user_id=1, name="Fruits", description="the fleshy seed-associated structures of a plant that are sweet or sour, and edible in the raw state")

session.add(cat1)
session.commit()

item1 = Item(user_id=1, name="Apple", description="Delicious and crunchy, apple fruit is one of the most popular and favorite fruits among the health conscious, fitness lovers who firmly believe in the concept of 'health is wealth'. This wonderful fruit is packed with rich phyto-nutrients that, in the true sense, indispensable for optimal health. Certain antioxidants in apple have several health promoting and disease prevention properties, and thereby, truly justifying the adage, 'an apple a day keeps the doctor away.'",
                     category=cat1)

session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Orange", description="Orange is a tropical to semitropical, evergreen, small flowering tree, growing to about 5 to 8 m tall, and bears seasonal fruits that measure about 3 inches in diameter and weigh about 100-150 g. Oranges are classified into two general categories, sweet and bitter, with the former being the type most commonly consumed type. Popular sweet-varieties include Valencia, Navel, Persian variety, and blood orange.",
                     category=cat1)

session.add(item2)
session.commit()

item3 = Item(user_id=1, name="Banana", description="Banana fruit is composed of soft, easily digestible flesh made up of simple sugars like fructose and sucrose that upon consumption instantly replenishes energy and revitalizes the body. Thus, for these qualities, it is one of popular quick-bites among athletes to get instant energy. It is also one of the recommended supplement food included in the treatment plan for under-nourished children.",
                     category=cat1)

session.add(item3)
session.commit()

item4 = Item(user_id=1, name="Blueberry", description="After many years of research on blueberry antioxidants and their potential benefits for the nervous system and for brain health, there is exciting new evidence that blueberries can improve memory.",
                     category=cat1)

session.add(item4)
session.commit()

item5 = Item(user_id=1, name="Cherry", description="Cherries are one of the very low calorie fruits. Nonetheless, they are rich source of phytonutrients, vitamins, and minerals. Both sweet as well as tart cherries are packed with numerous health benefiting compounds that are essential for wellness.",
                     category=cat1)

session.add(item5)
session.commit()

# Meats
cat2 = Category(user_id=1, name="Meats", description = "animal flesh that is eaten as food" )

session.add(cat2)
session.commit()


item1 = Item(user_id=1, name="Beef", description="Beef muscle meat can be cut into roasts, short ribs or steak (filet mignon, sirloin steak, rump steak, rib steak, rib eye steak, hanger steak, etc.) Some cuts are processed (corned beef or beef jerky), and trimmings, usually mixed with meat from older, leaner cattle, are ground, minced or used in sausages.",
                     category=cat2)

session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Duck", description="Duck meat is derived primarily from the breasts and legs of ducks. The meat of the legs is darker and somewhat fattier than the meat of the breasts, although the breast meat is darker than the breast meat of a chicken or a turkey. Being waterfowl, ducks have a layer of heat-insulating subcutaneous fat between the skin and the meat.",
                     category=cat2)

session.add(item2)
session.commit()

item3 = Item(user_id=1, name="Pork", description="Pork is the culinary name for meat from the domestic pig (Sus domesticus). It is the most commonly consumed meat worldwide,[1] with evidence of pig husbandry dating back to 5000 BC. Pork is eaten both freshly cooked and preserved. Curing extends the shelf life of the pork products. Ham, smoked pork, gammon, bacon and sausage are examples of preserved pork. Charcuterie is the branch of cooking devoted to prepared meat products, many from pork.",
                     category=cat2)

session.add(item3)
session.commit()

item4 = Item(user_id=1, name="Chicken", description="Chicken as a meat has been depicted in Babylonian carvings from around 600 BC.[3] Chicken was one of the most common meats available in the Middle Ages.[citation needed] It was eaten over most of the Eastern hemisphere and a number of different kinds of chicken such as capons, pullets and hens were eaten. It was one of the basic ingredients in the so-called white dish, a stew usually consisting of chicken and fried onions cooked in milk and seasoned with spices and sugar.",
                     category=cat2)

session.add(item4)
session.commit()

item5 = Item(user_id=1, name="Lamb", description="The meat of a lamb is taken from the animal between one month and one year old, with a carcase (carcass in American English) weight of between 5.5 and 30 kilograms (12 and 65 lbs). This meat generally is more tender than that from older sheep and appears more often on tables in some Western countries.",
                     category=cat2)

session.add(item5)
session.commit()

item5 = Item(user_id=1, name="Turkey", description="Turkeys are sold sliced and ground, as well as 'whole' in a manner similar to chicken with the head, feet, and feathers removed. Frozen whole turkeys remain popular. Sliced turkey is frequently used as a sandwich meat or served as cold cuts; in some cases where recipes call for chicken it can be used as a substitute. Ground turkey is sold just as ground beef, and is frequently marketed as a healthy alternative to beef.",
                     category=cat2)

session.add(item5)
session.commit()



# Fish
cat1 = Category(user_id=1, name="Fish", description = 'member of a paraphyletic group of organisms that consist of all gill-bearing aquatic craniate animals that lack limbs with digits.')

session.add(cat1)
session.commit()


item1 = Item(user_id=1, name="Salmon",
                     description="Salmon is a popular food. Classified as an oily fish, salmon is considered to be healthy due to the fish's high protein, high omega-3 fatty acids, and high vitamin D content.  Salmon is also a source of cholesterol.",
                     category=cat1)

session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Rainbow Trout",
                     description="Species of salmonid native to cold-water of the Pacific Ocean in Asia and North America",
                     category=cat1)

session.add(item2)
session.commit()

item3 = Item(user_id=1, name="Cod",
                     description="mild flavour and a dense, flaky white flesh",
                     category=cat1)

session.add(item3)
session.commit()

print "added items!"