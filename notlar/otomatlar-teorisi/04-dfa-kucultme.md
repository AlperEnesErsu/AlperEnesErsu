# 4 · DFA Küçültme (Minimization)

Aynı dili tanıyan DFA'lar içinde en az durumlu olan tektir (durum adları dışında). Küçültme, **ayırt edilemeyen** durumları birleştirir.

## Ayırt edilebilirlik

İki durum `p` ve `q` için bir `w` dizgisi varsa ve `δ(p, w)` ile `δ(q, w)`'den biri kabul, diğeri ret ise `p` ile `q` **ayırt edilebilir**. Böyle bir `w` yoksa eşdeğerdirler ve birleştirilebilirler.

## Yöntem (bölümleme)

1. Ulaşılamayan durumları sil.
2. Başlangıç bölümü: `{kabul durumları}`, `{ret durumları}`.
3. Her grubu her sembol için kontrol et: aynı gruptaki iki durum, aynı sembolle farklı gruplara gidiyorsa grubu böl.
4. Hiçbir grup bölünmeyene kadar 3. adımı tekrarla.
5. Her grup yeni DFA'da tek bir durumdur.

## Çözümlü örnek

Σ = {a, b}, `ab` ile biten dizgiler için gereğinden büyük bir DFA:

| Durum | a | b |
| --- | --- | --- |
| →A | B | C |
| B | B | D |
| C | B | C |
| *D | B | C |

- **Bölüm 0:** `{D}`, `{A, B, C}`
- **b ile kontrol:** A → C (ret), B → D (kabul), C → C (ret). B ayrılır.
- **Bölüm 1:** `{D}`, `{B}`, `{A, C}`
- **{A, C} kontrolü:** a ile ikisi de B'ye, b ile ikisi de C'ye gidiyor. Bölünme yok.

Sonuç (3 durum):

| Durum | a | b |
| --- | --- | --- |
| →{A,C} | B | {A,C} |
| B | B | D |
| *D | B | {A,C} |

## Tablo doldurma yöntemi (alternatif)

1. Her durum çifti için bir hücre aç.
2. Biri kabul, biri ret olan çiftleri işaretle.
3. `(p, q)` işaretsizken bir sembol onları işaretli bir çifte götürüyorsa `(p, q)`'yu da işaretle.
4. Değişiklik bitince işaretsiz kalan çiftler eşdeğerdir.

## Kendini test et

- [ ] Ulaşılamayan durumları neden önce silmek gerekir?
- [ ] "Tek sayıda a" dilini tanıyan 4 durumlu bir DFA kur, sonra 2 duruma küçült.
- [ ] İki DFA'nın aynı dili tanıyıp tanımadığını küçültme ile nasıl kontrol edersin?
