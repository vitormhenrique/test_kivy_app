from enum import Enum
from models.asset import Asset
from models.tag import TagValue, Tag
import pandas as pd

from peewee import *



# assets = Asset.select().select(Person, fn.COUNT(Pet.id).alias('pet_count'))
# assets = Asset.select().join(TagValue)

assets = Asset.select()

df = pd.DataFrame(assets.dicts())


tagval = TagValue.select(
    Asset.id,
    Asset.model,
    Asset.firmware,
    Asset.owner,
    TagValue.value,
    Tag.name
    ).join_from(TagValue,Asset).join_from(TagValue,Tag)

df_t = pd.DataFrame(tagval.dicts())

df_t.pivot_table('value', ['model', 'firmware', 'owner','id'], 'name')


df = df_t.set_index(['model', 'firmware', 'owner','id', 'name'], drop=True).unstack('name')

df = df.reset_index(level=['model','firmware', 'owner']).T.reset_index()

df = df.replace("value", "")

df["level_0"] = df["level_0"].astype(str) + df["name"]

df = df.drop(columns=['name','level_0']).T

# df.reset_index(level=['model','firmware', 'owner'])

# df.reset_index(level=['value'])


# for asset in assets:
#     tagval = TagValue.select(Tag.name.alias('tag_name'), TagValue.value).join(Tag).where(TagValue.asset==asset)
#     df_t = pd.DataFrame(tagval.dicts())

#     df_t.pivot_table('value')


# query_2 = TagValue.select()

# df2 = pd.DataFrame(query_2.dicts())

# query_3 = Tag.select()

# df = pd.DataFrame(query.dicts())
# df2 = pd.DataFrame(query_3.dicts())


# lst = [TagValue.tag, TagValue.asset]

# tags = TagValue.select(*lst)

# for tag in tags:
    # print(tag)


# tags = TagValue.select(Asset,Tag).select()
# tags = TagValue.select(Asset,Tag).select(TagValue.tag.name, TagValue.tag.value, TagValue.asset.model)

# tags = TagValue.select().group_by(Asset)

# print(tags)
