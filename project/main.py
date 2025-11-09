"""Anonymization demo tool

Usage (from project folder):
    python main.py --data ../data/dataset_original.xlsx --action search --name "Ana Julia Lima De Oliveira"
    python main.py --data ../data/dataset_original.xlsx --action anonymize --method swap --out ../data/out_swap.xlsx
    python main.py --data ../data/dataset_original.xlsx --action anonymize --method mask --out ../data/out_masked.xlsx
    python main.py --data ../data/dataset_original.xlsx --action augment --out ../data/out_augmented.xlsx

This script is a demonstration and educational - not for production use with real personal data.
"""
import argparse
import pandas as pd
from anonymizer import search_person, anonymize_swap, anonymize_mask, augment_weighted

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', required=True, help='path to input excel dataset')
    parser.add_argument('--action', required=True, choices=['search','anonymize','augment'])
    parser.add_argument('--name', help='name to search (exact match)')
    parser.add_argument('--method', choices=['swap','mask'], default='mask')
    parser.add_argument('--out', help='output path for anonymized/augmented file')
    args = parser.parse_args()

    df = pd.read_excel(args.data)

    if args.action == 'search':
        if not args.name:
            print('Provide --name for search')
            return
        results = search_person(df, args.name)
        print('Search results (first 10):')
        print(results.head(10).to_string(index=False))
    elif args.action == 'anonymize':
        if args.method == 'swap':
            out = anonymize_swap(df)
        else:
            out = anonymize_mask(df)
        if args.out:
            out.to_excel(args.out, index=False)
            print('Wrote anonymized data to', args.out)
        else:
            print(out.head(10).to_string(index=False))
    elif args.action == 'augment':
        out = augment_weighted(df, n_extra=500)
        if args.out:
            out.to_excel(args.out, index=False)
            print('Wrote augmented data to', args.out)
        else:
            print(out.shape)
if __name__ == '__main__':
    main()