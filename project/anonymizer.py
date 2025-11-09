import pandas as pd
import numpy as np
import random, hashlib
from faker import Faker
fake = Faker('pt_BR')

def search_person(df, name):
    # exact match on name; case-insensitive
    return df[df['name'].str.lower() == name.lower()]

def anonymize_swap(df, seed=42):
    np.random.seed(seed)
    df2 = df.copy()
    df2['phone'] = np.random.permutation(df2['phone'].values)
    df2['zipcode'] = np.random.permutation(df2['zipcode'].values)
    df2['account'] = np.random.permutation(df2['account'].values)
    df2['name'] = df2['name'].apply(lambda x: x.split()[0][0] + '. ' + fake.last_name())
    return df2

def hash_text(s):
    return hashlib.sha256(str(s).encode()).hexdigest()[:16]

def anonymize_mask(df):
    df2 = df.copy()
    df2['name_pseudo'] = df2['name'].apply(lambda x: fake.first_name() + ' ' + fake.last_name())
    df2['account_hash'] = df2['account'].apply(hash_text)
    df2['phone_mask'] = df2['phone'].astype(str).apply(lambda x: '***-***-' + ''.join([c for c in x if c.isdigit()])[-2:])
    mean, std = df2['balance'].mean(), df2['balance'].std()
    df2['balance_perturbed'] = (df2['balance'] * 0.8 + np.random.normal(loc=mean, scale=std*0.3, size=df2.shape[0])*0.2).round(2)
    return df2.drop(columns=['name','account','phone','address'])

def augment_weighted(df, n_extra=500):
    # Create additional synthetic records using weighted average of donors for numeric fields
    synthetic = []
    for i in range(n_extra):
        donors = df.sample(n=3, weights=np.abs(df['balance'])+1, replace=True)
        weights = np.array([0.6,0.3,0.1])
        balance = float((donors['balance'].values * weights).sum() + np.random.normal(scale=50))
        synthetic.append({
            'id': df.shape[0] + i + 1,
            'name': fake.name(),
            'sex': donors['sex'].iloc[0],
            'agency': donors['agency'].sample(n=1).iloc[0],
            'account': str(random.randint(100000,99999999)),
            'phone': fake.phone_number(),
            'address': fake.street_address(),
            'city': fake.city(),
            'state': fake.state_abbr(),
            'zipcode': fake.postcode(),
            'balance': round(balance,2)
        })
    return pd.concat([df, pd.DataFrame(synthetic)], ignore_index=True)