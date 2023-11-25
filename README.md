# Palindrome Game API
A Django REST API that provides endpoints for playing a palindrome game.

## Description
1. **User APIs(POST, PUT, DELETE /accounts/api/v1/user/)**:
   - User creation, updation and deletion.(These APIs will be used for user management.)
   - User Login(/admin/login/): Once a user login, then the user ccan invoke the Game and List functionality.
2. **Game APIs**:
   - Create Game(POST /game/api/v1/): This will initialize empty string and should return game-id.
   - Get Board(GET /game/api/v1/): This will return the value of string from the server. e.g. After create-game, the state of the string will be "" and after user invokes Update Board, the string will have some value.
   - UpdateBoard(PUT /game/api/v1/): Using this PAI, the user will append one character between 'a' to 'z' to string. Server should update the string and add one more random character. Once the length of the string is 6, it should return whether the string is palindrome or not.
3. **List of Games API**:
   - This API should list all game Ids created in the system.
  

## Visuals
<img width="784" alt="image" src="https://github.com/Sarveshk76/palindrome-game-api/assets/78719645/b3911ff9-6c9b-411d-96f7-79f17e24c296">

