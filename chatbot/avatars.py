import python_avatars as pa

option_style = ['CIRCLE', 'TRANSPARENT']

list_skin_color = ['TANNED','YELLOW','PALE','LIGHT','BROWN','DARK_BROWN','BLACK']
list_top_type = ['NONE', 'BIG_HAIR', 'BOB', 'BUN', 'STRAIGHT_1']
list_mouth_type = ['DEFAULT','CONCERNED','DISBELIEF','EATING','GRIMACE','SAD','SCREAM_OPEN','SERIOUS','SMILE','TONGUE','TWINKLE','VOMIT']
list_eye_type = ['DEFAULT','CLOSE','CRY','DIZZY','EYE_ROLL','HAPPY','HEARTS','SIDE','SQUINT','SURPRISED','WINK','WINK_WACKY']
list_accessories_type = ['DEFAULT','KURT','PRESCRIPTION_01','PRESCRIPTION_02','ROUND','SUNGLASSES','WAYFARERS']
list_clothe_type = ['BLAZER_SHIRT','BLAZER_SWEATER','COLLAR_SWEATER','GRAPHIC_SHIRT','HOODIE','OVERALL','SHIRT_CREW_NECK','SHIRT_SCOOP_NECK','SHIRT_V_NECK']

my_avatar = pa.Avatar(
    skin_color=eval('pa.SkinColor.%s' % skin),
    top=eval('pa.HairType.%s' % list_top_type[3]),
    mouth=eval('pa.MouthType.%s' % list_mouth_type[4]),
    eyes=eval('pa.EyeType.%s' % list_eye_type[5]),
    accessory=eval('pa.AccessoryType.%s' % list_accessories_type[6]),
    clothing=eval('pa.ClothingType.%s' % list_clothe_type[4]),
)

# Save to a file
my_avatar.render("my_avatar.svg")