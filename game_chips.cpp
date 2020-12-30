/*The following code is for the game of chips for two players.
The game begins with a number of chips in the pile.
Each player then takes a number of allowed chips to be taken per round.
Whoever takes the last chips looses the game.
*/
#include<iostream>
#include<ctime>
#include<cstdlib>

using namespace std;

const float MAX_TURN = 0.5;
const int MAX_CHIPS = 100;

int main()
{

	int chipsInPile = 0;
	int chipsTaken = 0;
	int maxPerTurn = 0;

	char userChoice;

	bool player1Turn = true;
	bool gameOver = false;

	string playerNames[2];

	//seeding the random number generator
	srand(time(0));

	//taking input of names and storing in an array
	cout << "Player 1 please enter your name: ";
	cin >> playerNames[0];
	cout << "\nThank you and good luck!" << endl << "Player 2 please enter your name: ";
	cin >> playerNames[1];
	cout << "\nThank you and good luck!";

	do
	{
		//assigning number of chips in the pile
		chipsInPile = (random() % MAX_CHIPS) + 1;
		cout << "This round will start with " << chipsInPile << " chips.";
		gameOver = false;
		
		while (gameOver == false)
		{

			do
			{
				//loop checks that the player takes valid number of chips
				maxPerTurn = chipsInPile * MAX_CHIPS ;

				if(player1Turn)
				{
					cout << playerNames[0] << " how many chips will you take?";
				}

				else
				{
					cout << playerNames[1] << " how many chips will you take?";
				}

				cout << "You can take upto: ";

				if(maxPerTurn == 0)
				{
					cout << "1\n";
				}
				else
				{
					cout << maxPerTurn << endl;
				}

				cin >> chipsTaken ;

			} while((chipsTaken > maxPerTurn) && (chipsInPile > 1));

			chipsInPile = chipsInPile - chipsTaken;
			cout << "There are " << chipsInPile << " chips left in the pile.";

			//when the game is over. Now determining the winner
			if(chipsInPile == 0)
			{
				gameOver = true;

				if(player1Turn)
				{
					cout << "Congratulations " << playerNames[1] << ", you have won the game!\n";
				}
				else
				{
					cout << "Congratulations " << playerNames[0] << ", you have won the game!\n";
				}
			}
			//otherwise changing the player's turn
			else
			{
				player1Turn = !player1Turn;
			}
		}
			//asking to play again or not
			cout >> "Do you want to play again? (Y/N): ";
			cin >> userChoice;

	} while ((userChoice == 'y') || (userChoice == 'Y'));

	return 0;
}
