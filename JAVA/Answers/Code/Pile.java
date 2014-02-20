/**
 * Subclass to CardCollection. This class represents the 13 piles of face-up cards in the Wristwatch
 * @author Jakob Moberg
 * @version Created Apr 8, 2013
 */

public class Pile extends CardCollection{
    
    /**Place card c first in the ArrayList cards. This represents the action of placing the card on the top of the pile. */
       
    public void placeCard(Card c)
    {
        cards.add(0,c);
    }
}