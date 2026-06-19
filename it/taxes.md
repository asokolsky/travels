---
title: Italian Taxes
parent: Italy
layout: page
---

Applicable ONLY if you are an Italian [tax resident](tax-residency.html).

Working assumption: examples are household-level planning estimates for a U.S.
citizen couple unless a section says otherwise. Tax-year references use 2025
income reported on 2026 forms where stated.

## What Is `Quadro W`?

`Quadro W` is the part of an Italian tax return used to disclose foreign assets
and calculate certain foreign-asset taxes. It is not an income category by
itself. Dividends, interest, capital gains, rent, or pension income may be
taxed elsewhere in the return, while the foreign account or asset that produced
the income may still belong in `Quadro W`.

For an Italian tax resident with U.S. assets, `Quadro W` is the place to think
about U.S. brokerage accounts, bank accounts, foreign real estate, and
crypto-assets. It is also where the return calculates IVAFE on foreign
financial assets and IVIE on foreign real estate when those taxes apply.

## Wealth Tax - Imposta sul Valore delle Attività Finanziarie all'Estero, IVAFE

Italian tax residents use `Quadro W` to report foreign investments and foreign
financial assets and, when due, to calculate IVAFE. The 730/2026 instructions
describe IVAFE as the tax on foreign financial products, bank accounts, and
savings books held abroad. The common investment-asset rate is 0.2% of value;
foreign bank accounts and special cases can be calculated differently, so use
the annual `Quadro W` instructions rather than treating the 0.2% rule as the
whole calculation.

## Foreign Real Estate - Imposta sul Valore degli Immobili situati all’Estero, IVIE

Italian tax residents also use `Quadro W` to calculate IVIE on foreign real
estate. A rough planning assumption is 0.76% of value per year, reduced by
available foreign property-tax credits and prorated for months of ownership.
The 730/2026 instructions include the IVIE fields, credits, ownership months,
and the €200 primary-residence detraction.

## Personal Income Tax - Imposta sul Reddito delle Persone Fisiche, IRPEF

### Current IRPEF Brackets

For 2025 income reported on `Modello 730/2026`, the national IRPEF brackets
are:

| Taxable income slice           | Rate | Gross IRPEF formula                      |
| ------------------------------ | ---- | ---------------------------------------- |
| Up to €28,000                  | 23%  | 23% of the full amount                   |
| Over €28,000 and up to €50,000 | 35%  | €6,440 + 35% of the amount over €28,000  |
| Over €50,000                   | 43%  | €14,140 + 43% of the amount over €50,000 |

These are national IRPEF rates before deductions, credits, regional
addizionale, municipal addizionale, and any substitute-tax regime. For a married
couple, apply the brackets separately to each spouse's taxable income; Italy
does not pool the couple's income into one shared bracket schedule.

### Regional and Municipal Addizionali

Regional and municipal addizionali are local IRPEF add-ons, separate from the
national IRPEF brackets above. They belong in the ordinary-IRPEF model for each
taxpayer. For a married couple, apply them separately to each spouse's taxable
income and tax domicile; they do not create a shared household bracket.

For 2025 income reported on `Modello 730/2026`, the MEF regional lookup gives
these regional addizionale rates:

| Taxable income slice           | Piemonte regional rate | Abruzzo regional rate |
| ------------------------------ | ---------------------- | --------------------- |
| Up to €15,000                  | 1.62%                  | 1.67%                 |
| Over €15,000 and up to €28,000 | 2.13%                  | 1.67%                 |
| Over €28,000 and up to €50,000 | 2.75%                  | 2.87%                 |
| Over €50,000                   | 3.33%                  | 3.33%                 |

For the same 2025 income year, the MEF municipal lookup and annual municipal
list give these municipal addizionale rates:

| Taxable income slice           | Torino municipal rate | Martinsicuro municipal rate |
| ------------------------------ | --------------------- | --------------------------- |
| Up to €15,000                  | 0.8%                  | 0.8%                        |
| Over €15,000 and up to €28,000 | 0.8%                  | 0.8%                        |
| Over €28,000 and up to €50,000 | 1.1%                  | 0.8%                        |
| Over €50,000                   | 1.2%                  | 0.8%                        |

Municipal exemption thresholds apply before the rate table: Torino exempts
taxable income up to €11,790, while MEF does not list a 2025 exemption
threshold for Martinsicuro.

A quick marginal-rate screen is therefore: Piemonte/Torino can add up to 4.53
percentage points on the top slice (3.33% regional + 1.2% municipal), while
Abruzzo/Martinsicuro can add up to 4.13 percentage points on the top slice
(3.33% regional + 0.8% municipal).

These local addizionali are for ordinary IRPEF. If a special substitute-tax
regime applies to some income, such as the Article 24-ter 7% pensioner regime,
model the substitute-tax income separately before adding local ordinary-IRPEF
rates.

### Filing as a Married Couple

Italy does not have a U.S.-style "married filing jointly" system where the
household pools income and applies one shared set of brackets. IRPEF is still
personal income tax. Each spouse is taxed on that spouse's own income, with
some family deductions and credits calculated around the family relationship.

A married couple or civil-union couple may be able to file a single
`Modello 730 in forma congiunta`, but that is mainly an administrative filing
convenience. For 730/2026, Agenzia Entrate says joint filing is available only
when both spouses have only income that can be reported on Form 730 and at
least one spouse can use Form 730. The joint return identifies one spouse as
the `dichiarante` and the other as the `coniuge dichiarante`.

Joint filing does not merge the spouses into one tax account. The 730/2026
instructions say that, even in a joint return, each spouse can decide how to
use the credit from that spouse's own return, and one spouse's credit cannot be
used to pay the other spouse's tax. For planning purposes, model the couple as
two taxpayers and then add the household totals.

### How Income Is Split Between Spouses

Start with legal ownership and who earned the income:

- Salary, pension, Social Security, professional income, and separate-activity
  income belong to the spouse who earned or received them.
- Separately owned bank, brokerage, pension, or real-estate assets generally
  belong to the legal owner.
- Jointly owned or co-owned assets are reported using each spouse's ownership
  percentage. For Italian real estate, the 730 instructions use a
  `percentuale di possesso`; for foreign assets in `Quadro W`, each joint owner
  reports the full asset value and that owner's percentage of ownership.
- If an asset is part of Italy's legal community property (`comunione legale`),
  TUIR Article 4 imputes the net income to each spouse 50/50, unless a
  different share is validly established under the Civil Code. The same article
  keeps the proceeds of each spouse's separate activity entirely with that
  spouse.
- Income from assets in a `fondo patrimoniale` is generally imputed half to
  each spouse under TUIR Article 4, with specific exceptions.

Being married does not automatically make one spouse a dependent. For 2025
income reported on 730/2026, a spouse can be treated as `fiscalmente a carico`
only if the spouse's total income is no more than €2,840.51 before deductible
charges. The spouse's tax code still has to be listed in the family section
even if the spouse is not tax-dependent.

## Investment Income - Capital Gains, Dividends, and Interest

Baseline rule for an Italian tax resident: Italy taxes worldwide investment
income unless a treaty rule or special substitute-tax regime changes the result.
For U.S. taxable brokerage accounts, this means the account may appear in
`Quadro W` for foreign-asset reporting and IVAFE, while the dividends,
interest, and realized capital gains are taxed in the income sections of the
return.

For a married couple, use the ownership rules above: separately owned accounts
belong to the owning spouse, and joint accounts are allocated by ownership
percentage.

Ordinary planning assumptions:

- Dividends from ordinary portfolio shares: `redditi di capitale` under TUIR
  Article 44; usually a 26% final withholding or substitute-tax item. Special
  rules can apply for pre-2018 profits, privileged-tax jurisdictions, business
  holdings, and some fund structures.
- Interest from bank accounts and bonds: `redditi di capitale` under TUIR
  Article 44; usually 26%. Interest on Italian government bonds and qualifying
  government/equivalent bonds is a major exception, commonly modeled at 12.5%.
- Capital gains from stocks, ETFs, funds, bonds, options, and other financial
  instruments: `redditi diversi` under TUIR Articles 67-68; usually 26% on net
  realized gains after eligible financial losses. Government/equivalent bond
  gains can get the 12.5% effective treatment through the reduced taxable base.

Important details:

- Dividends and interest are not just added to ordinary progressive IRPEF in
  the basic portfolio model; they are usually taxed through final withholding
  or substitute tax.
- If an Italian intermediary withholds the final tax, the item may not need the
  same return treatment as a foreign account with no Italian withholding.
- If the income is from a U.S. brokerage account with no Italian withholding,
  expect the tax preparer to classify the income in the return, often using
  the 730/2026 `Quadro D`, `Quadro M`, `Quadro T`, and `Quadro W` framework or
  the corresponding `Modello Redditi PF` schedules.
- Capital losses generally offset only eligible financial capital gains and
  similar `redditi diversi`, not dividend or interest income. TUIR Article 68
  allows excess losses to be carried forward against later eligible gains, but
  not beyond the fourth following tax period.
- Bond funds and ETFs are not automatically the same as holding government
  bonds directly. Confirm the fund-level treatment before assuming the 12.5%
  government-bond result.
- If the Article 24-ter 7% pensioner regime applies, qualifying foreign-source
  dividends, interest, and capital gains need to be modeled under that
  substitute-tax election instead of simply applying the ordinary 26% portfolio
  rule. Italian-source items and nonqualifying items still need separate review.
- U.S. citizenship does not remove the Italian tax-residence filing problem.
  The U.S. return, treaty positions, and foreign tax credit calculation still
  need to be modeled after the Italian classification is known.

## Real Estate - Imposta Municipale Unica, IMU

Imposta Municipale Unica (IMU) municipal property tax applies to second homes,
luxury properties, and non-residential real estate.

Source: Law 160/2019, Article 1, is the baseline national IMU statute; municipal
pages such as Torino's IMU page set local rates and filing/payment details.

### Primary Residence

As a Primary Residence: €0.

Standard, non-luxury primary homes (Category A/2 to A/7) are exempt from IMU.

Luxury primary residences in cadastral categories A/1, A/8, or A/9 remain
inside the IMU system.

### Second Homes

Second-home rough planning range: €2,600-€4,875.

The tax is determined using an official, government-registered value known as
the valore catastale, rather than its actual €500,000 market value:

```
IMU = Valore Catastale * Aliquota
```

Valore Catastale (Cadastral Value): The Rendita Catastale assigned to the
property by the Agenzia delle Entrate is revalued by 5%, and multiplied by a
coefficient of 160 for apartments in the 'A' category:

```
Valore Catastale = (Rendita Catastale + 5%) * Multiplier
```

Key Components of the Formula

- Rendita Catastale (Cadastral Income): A theoretical income value assigned to
  the property by the land registry, usually significantly lower than the market
  value.

- Multiplier: For standard residential properties, this is typically 160.

- Aliquota: Set locally by the municipality where the apartment is located.
  For rough planning, second-home rates often fall around 0.4% to 1.06%, but
  the municipal resolution is the source of truth.

For an apartment in Torino with a $500,000 market value, that is about €460,000
at the June 16, 2026 ECB reference rate, but IMU uses cadastral value rather
than market value.

[Torino IMU](https://www.comune.torino.it/amministrazione/ufficio-imu-gestione-rapporti-lutenza-imu)

## Example

Planning assumptions:

- Household income is $150,000, converted at the ECB reference rate for
  June 16, 2026 (€1 = $1.1594), or about €129,000.
- Income mix: about €74K of pension / Social Security income taxed as ordinary
  IRPEF income, plus about €27.7K of dividends and €27.7K of capital gains.
- The ordinary income is modeled as one spouse's income. If pension / Social
  Security income is split between spouses, calculate IRPEF and local
  addizionali separately for each spouse.

### Torino - Ordinary Regime

Rough back-of-the-envelope estimates for a couple living in Torino and earning
$150K:

- Pension + SS (~€74K): National progressive IRPEF before credits → ~€24,400
- Piemonte regional addizionale on the €74K ordinary IRPEF income → ~€1,920
- Torino municipal addizionale on the €74K ordinary IRPEF income → ~€750
- Dividends (~€27.7K): Flat 26% → ~€7,200
- Capital Gains (~€27.7K): Flat 26% → ~€7,200
- IVAFE (foreign investments): 0.2% of asset value (est.) → ~€200–€500
- IVIE (if you own foreign real estate): 0.76% of value (if applicable)
- Voluntary health-system contribution (SSN): Flat €2,000/year

The regional and municipal addizionali apply to ordinary IRPEF income, not to
the 26% flat-tax dividend and capital-gain items in this rough model. Torino's
municipal exemption does not help once taxable income is above €11,790.

**Total Estimated Taxes/Contributions: €43,700–€44,000/year**, before any
IVIE.
If the ordinary income is split evenly between spouses, the national IRPEF
piece would be materially lower because each spouse gets a separate bracket
stack.

### Martinsicuro - Article 24-ter 7% Regime

Martinsicuro is a qualifying 7% pensioner-regime municipality in the repo's
eligible comuni screen: Abruzzo, population 16,058,
below the 30,000-resident ceiling. Article 24-ter of the TUIR and the 730/2026
instructions say the option can apply a 7% substitute tax to foreign-source
income for the year of transfer and the next nine tax periods, if the taxpayer
meets the personal eligibility conditions.

For the same $150K couple, if Article 24-ter applies to the foreign-source
income:

- All qualifying foreign income (~€129K): flat 7% → ~€9,100
- Voluntary health-system contribution (SSN): €2,000
- **Total Estimated Taxes/Contributions: ~€11,100/year**

For comparison, if Article 24-ter does not apply and the €74K pension / Social
Security amount is ordinary IRPEF income, the local addizionali would be:

- Abruzzo regional addizionale on the €74K ordinary IRPEF income → ~€1,900
- Martinsicuro municipal addizionale on the €74K ordinary IRPEF income → ~€590
  (0.8% flat; MEF does not list a 2025 exemption threshold)
- Local addizionali subtotal → ~€2,490

The ordinary-regime local addizionali are slightly lower than Torino's, but in
this example Article 24-ter is materially lower than the ordinary-regime Torino
estimate.

## Double Taxation

Italy and the U.S. have a bilateral income-tax treaty, and U.S. citizens can
also use the foreign tax credit rules. That does not remove the need to file on
both sides when both filing systems apply.

The planning sequence is:

### 1. Italy Taxes First

- If you become Italian tax resident under Italian rules, Italy generally taxes
  worldwide income unless a treaty rule or special regime changes the result.
- Private pensions, Social Security, government-service pensions, dividends,
  interest, and capital gains need category-by-category treaty review. The
  U.S.-Italy treaty has special pension and social-security language in Article
  18 and the protocol, and separate rules for government service in Article 19.

### 2. Then File the U.S. Return

- As a U.S. citizen, you remain subject to U.S. tax on worldwide income. The
  treaty saving clause also lets the U.S. tax its citizens as if the treaty did
  not exist, except for specific treaty benefits such as the double-taxation
  relief article.
- You may claim a Foreign Tax Credit (FTC), usually on Form 1116, for qualified
  foreign income taxes paid or accrued.

### 3. Foreign Tax Credit

- It can reduce U.S. tax on the same foreign-source income. IRS Publication 514
  says the credit is intended to relieve double tax when the same foreign income
  is taxed by both countries.
- The credit is limited. It generally offsets only U.S. income tax in the
  relevant limitation category; it does not make foreign wealth taxes,
  property taxes, or every substitute tax automatically creditable.

Example:

- If your U.S. tax owed would have been $9,000
- And you paid €19,000 (~$20,000) to Italy
- You may owe zero additional U.S. income tax if the Italian tax is creditable
  and fits within the U.S. limitation category.
- You may not get a “refund,” but you avoid double payment.

### 4. Residual U.S. Tax Can Remain

- If Italy taxes an item at a lower rate than the U.S., if the tax is not
  creditable, or if the income lands in a separate limitation category with
  insufficient foreign tax, residual U.S. tax can remain.
- The 7% pensioner regime is especially worth modeling with an expat tax
  preparer because a low Italian substitute tax may not cover the full U.S.
  liability on every income category.

Use an expat tax preparer who understands the credit, treaty positions, and
reporting such as FBARs if you cross thresholds.

## Succession and Death Taxes

Italian succession tax is based mainly on the deceased person's residence,
asset location, and the beneficiary's relationship to the deceased. Citizenship
alone is not the main driver.

Under the succession-tax territoriality rule in D.Lgs. 346/1990:

| Deceased person's tax situation | Italian inheritance-tax reach |
| ------------------------------- | ----------------------------- |
| Resident in Italy at death      | Worldwide assets and rights   |
| Not resident in Italy at death  | Italian-situs assets only     |

Current planning rates are:

| Beneficiary relationship                         | Succession tax                                                        |
| ------------------------------------------------ | --------------------------------------------------------------------- |
| Spouse or direct-line relatives                  | 4% above a €1,000,000 allowance per beneficiary                       |
| Siblings                                         | 6% above a €100,000 allowance per beneficiary                         |
| Other relatives up to the statutory family range | 6%, generally without the close-family allowance                      |
| Other beneficiaries                              | 8%                                                                    |
| Beneficiary with severe disability               | Allowance can rise to €1,500,000 before the relationship rate applies |

If inherited assets include Italian real estate, mortgage and cadastral taxes
can also apply under D.Lgs. 347/1990. First-home relief can reduce those real
estate transfer taxes to fixed amounts, but that is a separate issue from the
succession-tax rate.

## Sources

Primary:

- [Agenzia Entrate: 730/2026 instructions for 2025 income, updated May 28, 2026](https://www.agenziaentrate.gov.it/portale/documents/20143/9764684/730_2026_istruzioni_+agg+28+05+2026.pdf/0965387c-8738-287a-9378-1d038b997833?t=1779979758734)
- [Agenzia Entrate: personal income tax rates and calculation](https://www.agenziaentrate.gov.it/portale/web/english/personal-income-tax-rates-and-calculation)
- [MEF: 2025 Piemonte regional IRPEF addizionale](https://www1.finanze.gov.it/finanze2/dipartimentopolitichefiscali/fiscalitalocale/addregirpef/addregirpef.php?anno=2025&reg=13)
- [MEF: 2025 Abruzzo regional IRPEF addizionale](https://www1.finanze.gov.it/finanze2/dipartimentopolitichefiscali/fiscalitalocale/addregirpef/addregirpef.php?anno=2025&reg=01)
- [MEF: 2025 Torino municipal IRPEF addizionale](https://www1.finanze.gov.it/finanze2/dipartimentopolitichefiscali/fiscalitalocale/addirpef_newDF/risultato.htm?lista=1&r=1&pagina=piemonte.htm&pr=TO&cc=L219&anno=2025)
- [MEF: 2025 Martinsicuro municipal IRPEF addizionale](https://www1.finanze.gov.it/finanze2/dipartimentopolitichefiscali/fiscalitalocale/addirpef_newDF/risultato.htm?lista=1&r=1&pagina=abruzzo.htm&pr=TE&cc=E989&anno=2025)
- [MEF: 2025 annual municipal IRPEF addizionale list, updated March 13, 2026](https://www.finanze.gov.it/export/sites/finanze/.galleries/Documenti/Fiscalita-locale/Elenco-annuale-addizionale-comunale-IRPEF-2025-13-marzo-2026.xlsx)
- [Normattiva: TUIR Article 4, spouses and minor children](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art4)
- [Normattiva: TUIR Article 44, redditi di capitale](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art44)
- [Normattiva: TUIR Article 67, redditi diversi](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art67)
- [Normattiva: TUIR Article 68, capital-gain calculation rules](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art68)
- [Normattiva: TUIR Article 24-ter, 7% pensioner regime](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art24ter)
- [Normattiva: D.L. 66/2014 Article 3, financial-income 26% rate and exceptions](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2014-04-24;66~art3)
- [Normattiva: Law 160/2019 Article 1, IMU rules](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2019-12-27;160~art1)
- [Normattiva: D.Lgs. 346/1990, succession and donation tax](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1990-10-31;346)
- [Normattiva: D.Lgs. 347/1990, mortgage and cadastral taxes](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1990-10-31;347)
- [IRS Publication 514, Foreign Tax Credit for Individuals, 2025 returns](https://www.irs.gov/pub/irs-pdf/p514.pdf)
- [IRS: U.S.-Italy income tax treaty](https://www.irs.gov/pub/irs-trty/italy.pdf)
- [ECB Data Portal: $/€ reference exchange rate, June 16, 2026](https://data-api.ecb.europa.eu/service/data/EXR/D.%55%53%44.%45%55%52.SP00.A?startPeriod=2026-06-16&endPeriod=2026-06-16)

Planning tools:

- [My IRPEF Calculator](https://docs.google.com/spreadsheets/d/1iVwUxg1oKGiDv__QlA2jpbPk5EE4NSAm05-NwRVN92E/edit?gid=0#gid=0)

Secondary:

- [PWC: Italy Taxes](https://taxsummaries.pwc.com/italy)
- [How to Calculate Inheritance Taxes](https://www.mylawyerinitaly.com/inheritance-tax-calculation/)
- [Choice of Law in Italian-American Cross-Border Successions](https://www.mylawyerinitaly.com/choice-of-law-in-italian-american-cross-border-successions/inheritance/)
- [Taxes for US expats](https://www.expatslivinginrome.com/taxes-for-us-expats-in-italy/)
- [Tax benefits of fiscal residence in Italy](https://www.expatslivinginrome.com/tax-benefits-fiscal-residence-italy/)
- [Expats living in Rome](https://www.expatslivinginrome.com/category/legal/taxes-1/)
- [taxing.it](https://taxing.it/technical-resources/)
