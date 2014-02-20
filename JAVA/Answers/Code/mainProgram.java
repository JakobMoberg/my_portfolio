    /**
     * This class is the main program for the "Wristwatch" solitaire implementation.
     * @author Jakob Moberg
     * @version Created Apr 8, 2013
     */
public class mainProgram{

    /**
     * The main method runs a number of games prints the percentage of won games. 
     * Takes either a single integer as args[] where the int represents the number
     * of MC simulation I.E("run mainProgram 100" runs 100 MC-runs). 
     * The methods defaults to a single MC run.
     */
    public static void main(String args[])
        
    {
        int nrSimRuns;
        int totalWon;
        double percentage;
        
        
        nrSimRuns=1;
        
//        Checks the args[] vector. If the input is bad format or has too many inputs  
//        the program breaks and error message is printed.
        
        if(args.length ==1){
            try{nrSimRuns=Integer.parseInt(args[0]);}
            
            catch(NumberFormatException ex)
            {
                System.out.println(args[0] + " is not an integer.Please try again");
                return;
            }
        }
        else if(args.length>1){
            System.out.println("This programs can only take 0 or 1 arguments");
            return;
        }
        totalWon=0;     
        int result;
        
//     Main loop
//     Each run creates and runs a single game of Wristwatch solitaire.        
        for(int i=1;i<=nrSimRuns;i++)
        {
            
            Game g=new Game();
            result=g.runGame();
            totalWon=totalWon + result;
            
        }
        
//    Percentage calculation and printing of results 
        percentage=(double) totalWon / nrSimRuns*100;
        System.out.println("Percentage of games won " + percentage + "%"); 
    }
}