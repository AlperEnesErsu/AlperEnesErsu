# 5 · Dönüşüm Örnekleri (adım adım)

Sınavda en çok puan getiren iki işlem: NFA → DFA ve DFA → düzenli ifade.

## Örnek 1 · NFA → DFA

Σ = {a, b}, `ab` içeren dizgiler için NFA:

| Durum | a | b |
| --- | --- | --- |
| →q0 | {q0, q1} | {q0} |
| q1 | ∅ | {q2} |
| *q2 | {q2} | {q2} |

Alt küme yapısı (ε geçişi yok, ε-kapanışı durumun kendisi):

| DFA durumu | a | b |
| --- | --- | --- |
| →{q0} | {q0, q1} | {q0} |
| {q0, q1} | {q0, q1} | {q0, q2} |
| *{q0, q2} | {q0, q1, q2} | {q0, q2} |
| *{q0, q1, q2} | {q0, q1, q2} | {q0, q2} |

- İçinde q2 olan kümeler kabul durumudur.
- Mümkün 8 kümeden yalnızca 4'üne ulaşılıyor; ulaşılmayanları yazmaya gerek yok.
- `{q0, q2}` ile `{q0, q1, q2}` ikisi de kabul ve aynı yerlere gidiyor: küçültmede birleşirler (bkz. [04-dfa-kucultme.md](04-dfa-kucultme.md)). Sonuç 3 durumlu DFA.

## Örnek 2 · DFA → düzenli ifade (GNFA)

Σ = {a, b}, `b` ile biten dizgiler:

| Durum | a | b |
| --- | --- | --- |
| →q0 | q0 | q1 |
| *q1 | q0 | q1 |

1. **GNFA kur:** Yeni başlangıç `s`, `s → q0` ε ile. Yeni kabul `f`, `q1 → f` ε ile.
2. **q0'ı sök:** q0'da `a` döngüsü var.
   - `s → q1`: `ε a* b` = `a*b`
   - `q1 → q1`: eski `b` döngüsü ∪ `q1 → q0 → q1` yolu = `b ∪ aa*b`
3. **q1'i sök:** `s → f` = `a*b (b ∪ aa*b)* ε`

Sonuç: `a*b(b ∪ aa*b)*`. Bu ifade `(a ∪ b)*b` ile aynı dili anlatır; sadeleştirilmiş hâli sınavda da kabul edilir.

## Örnek 3 · Düzenli ifade → NFA

`(ab ∪ a)*`

1. `ab` için iki oklu NFA, `a` için tek oklu NFA.
2. Birleşim: yeni başlangıçtan ε ile ikisine.
3. Yıldız: yeni başlangıç (aynı zamanda kabul), kabul durumlarından ε ile birleşim makinesinin başına.

## Kendini test et

- [ ] Örnek 1'deki NFA'ya `q1 → q0` ε oku eklenseydi tablo nasıl değişirdi?
- [ ] Örnek 2'de durumları ters sırayla (önce q1) sök. Aynı dili veren başka bir ifade bulmalısın.
- [ ] `(a ∪ b)*abb` için NFA kur ve DFA'ya çevir.
