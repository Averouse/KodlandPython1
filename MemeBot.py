import discord
import random
import os
from discord.ext import commands
import asyncio

# Membaca token dari file token.txt
try:
    with open("token.txt", "r") as f:
        token = f.read().strip()  # Menghapus spasi atau newline yang tidak diperlukan
except FileNotFoundError:
    print("Error: File 'token.txt' tidak ditemukan. Pastikan file tersebut ada di direktori yang sama.")
    exit()

# Mengatur intents dan prefix bot
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def meme(ctx):
    folder_path = 'meme'  # Folder tempat gambar disimpan

    # Memastikan folder 'meme' ada dan tidak kosong
    if not os.path.exists(folder_path):
        await ctx.send("Folder 'meme' tidak ditemukan. Pastikan folder tersebut ada.")
        return
    if not os.listdir(folder_path):
        await ctx.send("Folder 'meme' kosong. Tambahkan beberapa gambar terlebih dahulu.")
        return

    # Memilih gambar secara acak dari folder 'meme'
    nama_images = random.choice(os.listdir(folder_path))

    # Mengirim gambar kepada pengguna
    try:
        with open(f'{folder_path}/{nama_images}', 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture)
    except Exception as e:
        await ctx.send("Terjadi kesalahan saat mengirim gambar.")
        print(f"Error: {e}")

# Menjalankan bot
try:
    bot.run(token)
except discord.LoginFailure:
    print("Error: Token tidak valid. Periksa kembali token Anda.")