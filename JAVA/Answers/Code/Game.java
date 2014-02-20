import java.util.ArrayList;

/**     
 * This class represents an instace of a Game of Wristwatch solitaire.
 * @author Jakob Moberg
 * @version Created Apr 8, 2013
 */

public class Game
{
    /** parameter for keeping the deck used.*/
    private Deck deck;
    
    /** parameter for keeping the 13 piles of cards.*/
    private ArrayList <Pile> piles;
    
    /** parameter for keeping track of the active piles. Once a match is found for a pile the corresponding index 
      * is removed from openPiles. This parameter is used to get rid the number of iterations on allready closed piles */
    private ArrayList <Integer> openPiles;
    
    /** Constructor. Initializes a deck, shuffles it and creates the 13 piles together with the ArrayList openPiles that 
      * initially contains all integers in the interval [0,12] */
    Game()
    {
        Deck deck=new Deck();
        deck.shuffleDeck();
    
        piles=new ArrayList<Pile>();
        openPiles = new ArrayList<Integer>();
     
        for(int i=0 ; i <= 12 ;i++)
        {
         piles.add(new Pile());
         openPiles.add(i);   
        }
        
        this.deck=deck;
        this.piles=piles;
        this.openPiles=openPiles;
                
    }
    
    /**Prints the piles of the current game. Used during testing.*/
    public void printPiles()
    {
        for(Pile p:piles)
        {
            p.printString();
        }
        
    }
    /** Method for running the game*/
    
    public int runGame()
    {
        Card activeCard;
        int nrOfCards,result,i,pos,pileSize;
        i=0;
        result=0;
        nrOfCards= this.deck.getTotalCards();
     
 //     Loop for drawing a card and placing in the correct pile.
        
        while (nrOfCards>0) 
        {
          
           activeCard=deck.drawCard();
            
//        Determines the next pile to get a card.
          pileSize=openPiles.size();
            i = i % pileSize;
//        Since only Integer objects can be stored in ArrayList this conversion is needed.
            pos=openPiles.get(i).intValue();    
 
//          Checks if the drawn card matches the position.
            if(pos==activeCard.getRank())
            {
                deck.addCardCollectionToBottom(piles.get(pos));
                piles.get(pos).clearCards();
                piles.get(pos).placeCard(activeCard);
                
//           Closes the pile. 
                openPiles.remove(i);
                
//          Checks if All the piles are closed and the solitaire is won. 
                if(openPiles.size()==0)
                {  
                    result=1;
                    break;
                }
                
            }
//            if no match is found the card is placed in the current pile.
            else 
            {
                piles.get(pos).placeCard(activeCard);
                i++;
            }

            nrOfCards=deck.getTotalCards();
          
        }
       
        return result;
    }
}