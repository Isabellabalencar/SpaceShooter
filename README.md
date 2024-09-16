# Space Shooter Game

This is a simple **Space Shooter** game developed using **Pygame**, where the player controls a spaceship and must destroy enemies by shooting bullets. The game includes basic mechanics like movement, shooting, and scoring, with enemies randomly appearing on the screen.

Este é um jogo simples de **Space Shooter** desenvolvido com **Pygame**, onde o jogador controla uma nave espacial e deve destruir inimigos disparando balas. O jogo tem mecânicas básicas de movimento, disparo e pontuação, com inimigos que aparecem aleatoriamente na tela.

## Features

- **Player Movement**: The player can move left and right using the arrow keys.
- **Shooting Bullets**: The player can shoot bullets by pressing the `SPACE` key. Each shot is unique and can only be repeated after releasing the key.
- **Enemies**: Enemies appear randomly at the top of the screen and move downward. If an enemy reaches the bottom of the screen, the player loses a life.
- **Scoring**: The player earns points by destroying enemies with the bullets.
- **Lives**: The player starts with 3 lives. If all lives are lost, the game ends.
- **Main Menu**: Before starting the game, the player can press `UP` to begin.
- **Restarting the Game**: After losing, the player can press `R` to restart the game.

- **Movimentação do jogador**: O jogador pode se mover para a esquerda e para a direita usando as teclas direcionais.
- **Disparo de balas**: O jogador pode disparar balas pressionando a tecla `SPACE`. Cada disparo é único e só pode ser repetido após soltar a tecla.
- **Inimigos**: Inimigos aparecem aleatoriamente na parte superior da tela e se movem para baixo. Se um inimigo atingir a parte inferior da tela, o jogador perde uma vida.
- **Pontuação**: O jogador ganha pontos ao destruir inimigos com as balas disparadas.
- **Vida**: O jogador começa com 3 vidas. Se todas as vidas forem perdidas, o jogo termina.
- **Menu inicial**: Antes do início do jogo, o jogador pode pressionar `UP` para começar.
- **Reinício do jogo**: Quando o jogador perde, pode pressionar `R` para reiniciar o jogo.

## Controls

- `←` **Left Arrow**: Move the spaceship to the left.
- `→` **Right Arrow**: Move the spaceship to the right.
- `SPACE` **Space Bar**: Shoot a bullet.
- `UP` **Up Arrow**: Start the game from the main menu.
- `R` **R Key**: Restart the game after losing.

- `←` **Seta Esquerda**: Move a nave para a esquerda.
- `→` **Seta Direita**: Move a nave para a direita.
- `SPACE` **Barra de Espaço**: Dispara uma bala.
- `UP` **Seta para Cima**: Inicia o jogo a partir do menu.
- `R` **Tecla R**: Reinicia o jogo após o término.

## How to Play

1. When the game starts, a menu screen will appear. Press the `UP` arrow to start playing.
2. Use the arrow keys `←` and `→` to move your spaceship sideways.
3. Press `SPACE` to shoot bullets and destroy enemies appearing at the top of the screen.
4. Each time an enemy reaches the bottom of the screen, you lose a life. The game ends when all lives are lost.
5. After losing, you can press `R` to restart the game.

1. Ao iniciar o jogo, uma tela de menu aparecerá. Pressione a seta `UP` para começar a jogar.
2. Use as teclas direcionais `←` e `→` para mover sua nave para os lados.
3. Pressione `SPACE` para disparar balas e destruir os inimigos que aparecem no topo da tela.
4. Cada vez que um inimigo atinge a parte inferior da tela, você perde uma vida. O jogo termina quando todas as vidas forem perdidas.
5. Ao perder, você pode pressionar `R` para reiniciar o jogo.

## Requirements

- **Python 3.x**: Make sure Python 3.x is installed on your system.
- **Pygame**: The game uses the Pygame library. You can install it by running the following command:

```bash
pip install pygame

- **Python 3.x**: Certifique-se de que o Python 3.x está instalado no seu sistema.
- **Pygame**: O jogo utiliza a biblioteca Pygame. Você pode instalá-la usando o comando:

```bash
pip install pygame


##Project Structure

/SpaceShooter
│
├── assets/                # Folder containing player and enemy images
│   ├── player.png         # Player's spaceship image
│   └── enemy.png          # Enemy's image
│
├── main.py                # Main game file
└── README.md              # This documentation file

/SpaceShooter
│
├── assets/                # Pasta contendo as imagens do player e dos inimigos
│   ├── player.png         # Imagem da nave do jogador
│   └── enemy.png          # Imagem dos inimigos
│
├── main.py                # Arquivo principal do jogo
└── README.md              # Este arquivo de documentação


