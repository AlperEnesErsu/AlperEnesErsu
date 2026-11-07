# 6 · Deneme Sınavı

Süre: 60 dakika. Önce cevapları gizleyip çöz, sonra kontrol et.

## Sorular

1. Σ = {0, 1}. 0 sayısı 3'e bölünebilen dizgileri tanıyan DFA'yı çiz.
2. Σ = {0, 1}. `11` içermeyen dizgiler için bir düzenli ifade yaz.
3. `L = {aⁿbᵐ | n ≥ m ≥ 0}` düzenli midir? Kanıtla.
4. Doğru / yanlış:
   - a) Her NFA'nın eşdeğer bir DFA'sı vardır.
   - b) `∅* = ∅`
   - c) Düzenli dillerin kesişimi düzenlidir.
   - d) Düzenli olmayan iki dilin birleşimi düzenli olamaz.
5. Σ = {a, b}. `ab` alt dizgisi ile `ba` alt dizgisinin aynı sayıda geçtiği dizgilerin dili düzenli midir?
6. `(0 ∪ 1)*01` için en küçük DFA kaç durumludur?

---

## Cevaplar

<details>
<summary>Göstermek için tıkla</summary>

**1.** Üç durum: `r0, r1, r2` (0 sayısının 3'e göre kalanı). `0` ile `rᵢ → r₍ᵢ₊₁₎ mod 3`, `1` ile durum değişmez. Başlangıç ve kabul `r0`.

**2.** `(0 ∪ 10)*(ε ∪ 1)`. Her 1'in arkasından ya 0 gelir ya da dizgi biter.

**3.** Düzenli değil. `s = aᵖbᵖ` seç. `|xy| ≤ p` olduğundan `y = aᵏ`, `k > 0`. `i = 0` ile `aᵖ⁻ᵏbᵖ`: a sayısı b sayısından az, dilde değil. (Burada yukarı pompalamak işe yaramaz; aşağı pompalamak gerekir.)

**4.**
- a) Doğru (alt küme yapısı).
- b) Yanlış: `∅* = {ε}`.
- c) Doğru (çarpım makinesi).
- d) Yanlış: `{0ⁿ1ⁿ}` ile tümleyeninin birleşimi `Σ*`'dır, düzenli.

**5.** Düzenlidir. `ab` ve `ba` geçişleri sırayla gelir, sayıları en fazla 1 farklıdır. Eşitlik ancak dizgi aynı sembolle başlayıp bitiyorsa (ya da boşsa) sağlanır: `ε ∪ a ∪ b ∪ aΣ*a ∪ bΣ*b`.

**6.** 3 durum: "sonda hiçbir şey yok / sonda 0 / sonda 01".

</details>

## Kendimi değerlendirme

- [ ] 6 sorunun en az 5'ini doğru yaptım.
- [ ] Pompalamada `i = 0` gerekip gerekmediğini fark ettim.
- [ ] 5. soruda dilin düzenli olduğunu sezip kanıtlayabildim.
