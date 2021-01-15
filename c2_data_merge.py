import pandas as pd

d1 = pd.read_json('100m_data_female.json')
d2 = pd.read_json('100m_data_male.json')
d3 = pd.read_json('500m_data_female.json')
d4 = pd.read_json('500m_data_male.json')
d5 = pd.read_json('1000m_data_female.json')
d6 = pd.read_json('1000m_data_male.json')
d7 = pd.read_json('2000m_data_female.json')
d8 = pd.read_json('2000m_data_male.json')
d9 = pd.read_json('5000m_data_female.json')
d10 = pd.read_json('5000m_data_male.json')
d11 = pd.read_json('6000m_data_female.json')
d12 = pd.read_json('6000m_data_male.json')
d13 = pd.read_json('10000m_data_female.json')
d14 = pd.read_json('10000m_data_male.json')
d15 = pd.read_json('21097m_data_female.json')
d16 = pd.read_json('21097m_data_male.json')
d17 = pd.read_json('42195m_data_female.json')
d18 = pd.read_json('42195m_data_male.json')
d19 = pd.read_json('100000m_data_female.json')
d20 = pd.read_json('100000m_data_male.json')


df = pd.concat([d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16,d17,d18,d19,d20])

df.to_csv('all_data.csv',index=False,encoding='utf-8')