import java.util.ArrayList;
import java.util.Collections;
/**
 * Subclass to CardCollection. This class represents the main deck
 * @author Jakob Moberg
 * @version Created Apr 8, 2013
 */
public class Deck extends CardCollection{
   /** Constructor
    * Initializes and populates the deck. 
    */
    Deck()
    {
        cards=new ArrayList<Card>(); 
        Card tempCard;

        for(int i=0; i<=12;i++)
        {
            for(int k=0; k<=3; k++)
            {
                cards.add(new Card(k,i));
            }
        }
            
    }
    
    /** Method for shuffling the cards in deck
     */
    public void shuffleDeck()
    {
        //using fisher-yates shuffle for generating of random permutation of the ArrayList cards.
       Collections.shuffle(cards); 
    }
    
    /**Method for drawing a card.  
     * The drawn card is returned and removed from the cards ArrayList.
     */
    
      public Card drawCard()
    {     
        return cards.remove(0);
    }
}
