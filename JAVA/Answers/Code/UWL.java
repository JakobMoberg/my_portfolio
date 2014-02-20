import java.util.Random;

public class UWL{

    public static void main(String args[]){
  
     Random randnum = new Random(System.nanoTime());
     int nrSim;
     double expValue,payout,totalPayout;
     payout=0;
     totalPayout=0;
     nrSim=1000000;
     
     for(int i=1;i<=nrSim;i++)
     {
         payout=uwlPayout(randnum);
         totalPayout=totalPayout + payout;
     }
     expValue=(double)totalPayout/nrSim;
     
        System.out.println("Exp value:" + expValue);
    }
    
    public static double uwlPayout(Random r){
        double payment;
        int event;
        payment=0;
        event=r.nextInt(10);
        
        switch(event){
            case 0: payment=9;
            break;
            case 1: payment=9;
            break;
            case 2: payment=18;
            break;
            case 3: payment=uwlPayout(r)+uwlPayout(r);
            break;
        }
        
        return payment;
     }
}