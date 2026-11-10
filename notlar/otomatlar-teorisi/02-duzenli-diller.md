# 2 · Düzenli Diller, Kapanış ve Düzenli İfadeler

## Düzenli dil

Bir dili tanıyan bir DFA (ya da NFA) varsa dil **düzenlidir**.

## Kapanış özellikleri

Düzenli diller şu işlemler altında kapalıdır:

| İşlem | Nasıl gösterilir |
| --- | --- |
| Birleşim `A ∪ B` | Yeni başlangıçtan ε ile iki makineye (NFA) |
| Birleştirme `A ∘ B` | A'nın kabul durumlarından ε ile B'nin başlangıcına |
| Yıldız `A*` | Yeni başlangıç kabul durumu; kabul durumlarından ε ile eski başlangıca |
| Kesişim `A ∩ B` | Çarpım makinesi: durumlar (p, q) çiftleri |
| Tümleme `Ā` | DFA'da kabul/ret yer değiştirir |

> Yıldızda yeni başlangıç durumu eklemek şart: eski başlangıcı kabul yapmak, istenmeyen dizgileri kabul ettirebilir.

## Düzenli ifadeler

Öncelik: `*` > birleştirme > `∪`

| İfade | Dil |
| --- | --- |
| `Σ*1Σ*` | en az bir 1 içerenler |
| `(ΣΣ)*` | çift uzunluklular |
| `0*10*` | tam bir tane 1 |
| `(0 ∪ ε)1*` | `01*` ∪ `1*` |
| `1*∅` | `∅` |
| `∅*` | `{ε}` |

## Dönüşümler

- **İfade → NFA:** Her parça için küçük NFA kur, kapanış yapılarıyla birleştir.
- **DFA → İfade:** Genelleştirilmiş NFA (GNFA) kur; yeni başlangıç ve tek kabul durumu ekle, durumları birer birer sök. `qi → qrip → qj` yolu için etiket: `R1 (R2)* R3 ∪ R4`.

## Çözümlü sorular

**S1.** Σ = {a, b}, aynı sembolle başlayıp biten dizgiler: `a ∪ b ∪ aΣ*a ∪ bΣ*b`.
Uzunluk en az 2 isteniyorsa ilk iki terim düşer: `aΣ*a ∪ bΣ*b`.

**S2.** `ab` ya da `ba` içermeyen dizgiler (Σ = {a, b, c}): sembol değişimi yalnızca `c` üzerinden olabilir. Tuzak durumuna `a`dan hemen sonra `b` ya da `b`den hemen sonra `a` ile girilir.

**S3.** "Çift sayıda a VE tek sayıda b": çarpım makinesi, 2 × 2 = 4 durum. Kabul: (çift a, tek b).

## Kendini test et

- [ ] `(a ∪ b)*` ile `a* ∪ b*` aynı mı? Bir ayırt edici dizgi bul.
- [ ] Kesişimi kapanış tablosundaki diğer işlemlerle (De Morgan) nasıl yazarsın?
- [ ] İki durumlu bir DFA'yı GNFA yöntemiyle ifadeye çevir.
