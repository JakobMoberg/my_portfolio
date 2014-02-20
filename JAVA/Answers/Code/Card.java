
/**     
 * This class represents a Card. Standard implementation.
 * @author Jakob Moberg 
 * @version Created Apr 8, 2013
 */
public class Card
{
    /**int parameter for representing the rank of the card  */
   
    private int rank; 
    /**int parameter for representing the suit of the card */
    private int suit;
    
    private static String[] suits= { "Spades", "Hearts", "Diamonds", "Clubs" };
    private static String[] ranks= { "A","2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"};
    /**
     Constructor
     @param suit
      * int representation of suit. 
      * int -> str,
      * 
      * 0 -> "Spades",
      * 1 -> "Hearts",
      * 2 -> "Diamonds",
      * 3 -> "Clubs"
     @param rank
      *int representation of rank.
      * int-> str,
      * 
      * 0 -> "A",
      * 1 -> "2",
      * 2 -> "3",
      * 3 -> "4", 
      * 4 -> "5", 
      * 5 -> "6", 
      * 6 -> "7", 
      * 7 -> "8", 
      * 8 -> "9", 
      * 9 -> "10", 
      * 10 -> "J", 
      * 11 -> "Q", 
      * 12  -> "K"*/
    Card(int suit, int rank)
    {
        this.rank=rank;
        this.suit=suit;
    }
    
    /** generates a String version of the Card. The output is of the form "J of Spades".*/
        public @Override String toString()
    {
          return ranks[rank] + " of " + suits[suit];
    }
   
    /** gets the int repesentation of rank.*/
        public int getRank(){
            return rank;
        }
        
   /** gets the int repesentation of suit.*/
        public int getSuit(){
            return suit;
        }
}
