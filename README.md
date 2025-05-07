# API-Spotify
Claro, aquí tienes la traducción al inglés del documento:

---

# 🎵 Spotify Exploration

## 📜 Overview

As part of the project, the Spotify API was integrated to obtain relevant information about artists and their performance on the platform. The process initially focused on three key types of data:

* 👉 **Tracks of the Year**
* 👉 **TOP 100 Artists – Global and Colombia**

---

## 🎧 1. Retrieving Information via Tracks of the Year

This section focuses on tracks released in the current year, extracting the most important information about the artists associated with each release.

### Information retrieved:

* 🎤 Artist ID
* 👩‍🎤 Artist name
* 🌟 Artist popularity
* 👥 Number of followers
* 🎶 Music genres
* 📸 Artist image
* 🎶 Track ID
* 🎧 Track name
* 🌟 Track popularity
* 📅 Track release date
* 📀 Album the track belongs to

---

### 🎤 What does artist and track popularity mean?

#### Artist Popularity:

A value between **0 and 100**. It's not solely based on streams, but also includes:

* 🎶 **Streams**: Total number of plays
* 💬 **Engagement**: Saves, shares, playlist adds
* ⏳ **Recency**: More weight given to recent activity
* 📋 **Playlist Inclusions**: Presence in popular playlists

💡 *This metric updates constantly and is useful for marketing and outreach strategies.*

---

#### 🎶 Track Popularity:

A value between **0 and 100**. Calculated based on:

* 🎧 **Streams**: Total number of plays
* ⏳ **Recency**: More recent tracks may score higher
* 📋 **Playlist Inclusions**: Inclusion in relevant playlists

⚠️ *It does not update in real time; there may be a slight delay in data reflection.*

---

### 📌 Sample Extracted Data (Tracks of the Year)

| track\_id              | track\_name                           | track\_popularity | album\_name                           | release\_date | artist\_id             | artist\_name   | artist\_popularity | followers  | genres                     | image\_url                                                               |
| ---------------------- | ------------------------------------- | ----------------- | ------------------------------------- | ------------- | ---------------------- | -------------- | ------------------ | ---------- | -------------------------- | ------------------------------------------------------------------------ |
| 3U21A07gAloCc4P7J8rxcn | Shakira: Bzrp Music Sessions, Vol. 53 | 92                | Shakira: Bzrp Music Sessions, Vol. 53 | 2023-01-11    | 0EmeFodog0BfCgMzAIvKQp | Shakira        | 88                 | 33,700,000 | pop, reggaeton, latin pop  | ![img](https://i.scdn.co/image/ab6761610000e5eb1b7a13e2dbed1fbfa99b8c35) |
| 0yLdNVWF3Srea0uzk55zFn | Ella Baila Sola                       | 95                | Genesis                               | 2023-04-07    | 12GqGscKJx3aE4t07u7eVZ | Eslabon Armado | 85                 | 9,200,000  | regional mexican, corridos | ![img](https://i.scdn.co/image/ab6761610000e5eb75b06014fc65a4706714c96b) |
| 2LRoIwlKmHjgvigdNGBHNo | La Bebe                               | 90                | La Bebe (Remix)                       | 2023-03-17    | 1SupJlEpv7RS2tPNRaHViT | Yng Lvcas      | 80                 | 4,100,000  | reggaeton, latin trap      | ![img](https://i.scdn.co/image/ab6761610000e5ebb6476c81275f2350f63b0400) |

---

## 🌍 2. Retrieving Information via the TOP 100 Artists (Global and Colombia)

Data was extracted from artists featured in unofficial but relevant and weekly-updated playlists targeting the market.

### Playlists Used:

* 🇨🇴 **Colombia TOP 100** → Playlist ID: `6h6uzoRBXnkjeoEjwiX27R`
* 🌐 **Global TOP 100** → Playlist ID: `0sDahzOkMWOmLXfTMf2N4N`

---

### 📌 Sample Extracted Data (TOP 100 Global and Colombia)

\| track\_id         | track\_name     | track\_popularity | album\_name               | release ...

(If you’d like me to finish or polish the last table or add anything else, just let me know!)
