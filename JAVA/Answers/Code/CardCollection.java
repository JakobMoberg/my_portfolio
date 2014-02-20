import java.util.ArrayList;
/**     
 * This class an abstract class for handling a collection of Card objects.
 * @author Jakob Moberg
 * @version Created Apr 8, 2013
 */

public abstract class CardCollection{
    /**ArrayList for keeping the card objects. */
    protected ArrayList <Card> cards;
    
     /**Constructor. Initilizes the cards ArrayList */
    CardCollection()
    {
        cards=new ArrayList<Card>();     
    }
    
     /**Prints the card objects in cards. Mainly used during the testing.*/
    public void printString()
    {
        System.out.println(cards.toString());
    }
    
    /**Returns the number of Card objects in cards*/
    public int getTotalCards()
    {
        return cards.size();
    }
    
      /**Returns the ArrayList cards*/
    public ArrayList <Card> getCards()
    { 
        
        return (ArrayList <Card>) cards.clone();
    }
    
       /**Adds CardCollection c to the end of the current instance of the class.
         * @param c                 CardCollection that is added to the end of this.cards
         */
    
        public void addCardCollectionToBottom(CardCollection c)
    {
        cards.addAll(c.getCards());
    }
     
          /**Clears the cards ArrayList.*/
    public void clearCards()
    {
        cards.clear();
    }
}