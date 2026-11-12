# 3 · Pompalama Önsavı ve Genel Tekrar

## Pompalama önsavı

A düzenliyse bir `p` (pompalama uzunluğu) vardır öyle ki `|s| ≥ p` olan her `s ∈ A`, `s = xyz` şeklinde bölünebilir ve:

1. Her `i ≥ 0` için `x yⁱ z ∈ A`
2. `|y| > 0`
3. `|xy| ≤ p`

**Neden doğru:** p durumlu DFA, p sembol okurken p+1 durumdan geçer; güvercin yuvası ilkesine göre bir durum tekrar eder. Tekrar eden döngü `y`dir.

## Düzenli olmadığını gösterme kalıbı

1. A'nın düzenli olduğunu varsay, `p` verilsin.
2. `|s| ≥ p` olan, `p`'ye bağlı bir `s` seç.
3. Koşul 3 sayesinde `y`'nin nerede olduğunu daralt.
4. Bir `i` bul, `x yⁱ z ∉ A`. Çelişki.

> Önsav yalnızca **düzenli olmadığını** göstermek için kullanılır. Pompalanabilmek düzenli olmayı kanıtlamaz.

## Çözümlü sorular

**S1.** `A = {0ⁿ1ⁿ | n ≥ 0}` düzenli değildir.
`s = 0ᵖ1ᵖ` seç. `|xy| ≤ p` olduğundan `y` yalnızca 0'lardan oluşur. `i = 2` için 0 sayısı 1 sayısını geçer, `xyyz ∉ A`.

**S2.** `B = {ww | w ∈ {0,1}*}` düzenli değildir.
`s = 0ᵖ1 0ᵖ1` seç (`0ᵖ0ᵖ` seçmek işe yaramaz, o pompalanabilir). `y` ilk 0 bloğunda; pompalayınca iki yarı eşitliği bozulur.

**S3.** `C = {w | w'de eşit sayıda 0 ve 1}` düzenli değildir.
Kısa yol: `C ∩ 0*1* = {0ⁿ1ⁿ}`. C düzenli olsaydı kesişim de düzenli olurdu (kapanış). Çelişki.

## Genel tekrar: sık yapılan hatalar

- DFA'da bir sembolün okunu unutmak (tuzak durumu eksik).
- `∅` ile `{ε}`'yi karıştırmak.
- NFA'yı DFA'ya çevirirken ε-kapanışı almayı unutmak.
- Pompalamada `s`'yi `p`'ye bağlı seçmemek ya da `y`'yi kendin seçmek. `y`yi rakip seçer, sen tüm bölünmeleri ele almalısın.

## Kendini test et

- [ ] `{aⁿ | n asal}` için hangi `s` ve hangi `i`?
- [ ] `{0ⁿ1ᵐ | n ≠ m}` düzenli mi? Kapanış ile göster.
- [ ] Sonlu her dil düzenli midir? Neden pompalama önsavıyla çelişmez?
