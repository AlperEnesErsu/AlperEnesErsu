# 1 · Sonlu Otomatlar (DFA ve NFA)

## Temel kavramlar

- **Alfabe (Σ):** Sonlu sembol kümesi.
- **Dizgi:** Sembollerin sonlu dizisi. `ε` uzunluğu 0 olan boş dizgi.
- **Dil:** Dizgilerden oluşan herhangi bir küme.
- `∅` hiç dizgi içermez; `{ε}` tek elemanı boş dizgi olan dildir. İkisi farklıdır.

## DFA

DFA = (Q, Σ, δ, q0, F)

- `Q`: sonlu durumlar, `δ : Q × Σ → Q`, `q0`: başlangıç, `F ⊆ Q`: kabul durumları.
- Her durumdan **her sembol için tam bir ok** çıkar.
- **Tuzak durumu:** Girilince çıkılmayan, kabul etmeyen durum.
- **Tümleme:** Kabul ve ret durumları yer değiştirirse makine dilin tümleyenini tanır (yalnızca DFA'da güvenli).
- Durumu "şimdiye kadar neyi hatırlamam gerekiyor?" sorusunun cevabı gibi düşün.

## NFA

- Bir durumdan aynı sembolle birden fazla yere gidilebilir, hiç ok olmayabilir, `ε` ile sembol okumadan geçilebilir.
- Dizgi, **en az bir yol** kabul durumunda bitiyorsa kabul edilir.
- NFA ile DFA aynı dil sınıfını tanır; NFA sadece daha kısa yazılır.

## NFA → DFA (alt küme yapısı)

1. Başlangıç: `E(q0)` (q0'dan ε ile ulaşılabilen her durum).
2. Her yeni küme `S` ve her sembol `a` için: `E(⋃ δ(q, a))`, `q ∈ S`.
3. İçinde NFA kabul durumu bulunan her küme kabul durumudur.
4. Boş küme `∅` tuzak durumudur.

En kötü durumda n durumlu NFA 2ⁿ durumlu DFA verir.

## Çözümlü sorular

**S1.** Σ = {a, b}, `bb` ile biten dizgiler için DFA.

| Durum | a | b | Anlamı |
| --- | --- | --- | --- |
| →q0 | q0 | q1 | sonda b yok |
| q1 | q0 | q2 | sonda tek b |
| *q2 | q0 | q2 | sonda bb |

`a` gelince bb dizisi bozulur, başa dönülür.

**S2.** Σ = {0, 1}, tek sayıda 1 içeren dizgiler: iki durum yeter (çift/tek). Kabul durumu "tek". Çift sayı için kabul durumu q0 olur.

**S3.** "Sondan üçüncü sembolü 1 olan dizgiler" için NFA 4 durumla yazılır; eşdeğer DFA en az 8 durum ister. 2ⁿ patlamasının klasik örneği.

## Kendini test et

- [ ] Bir durum hem başlangıç hem kabul olabilir mi?
- [ ] NFA'da tümleme neden doğrudan çalışmaz?
- [ ] `{ε}` dilini tanıyan en küçük DFA'yı çiz.
