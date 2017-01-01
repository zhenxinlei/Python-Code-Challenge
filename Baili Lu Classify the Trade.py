def classify(trades,lables,new_trades):
     green_number = 0;
     red_number = 0;
     for i in range(lables.__len__()):
          if(lables[i] == "green"):
               green_number = green_number+1;
          else:
               red_number = red_number+1;

     count = 0;
     profit_green =0.0;
     risk_green =0.0;
     latency_green= 0.0;
     profit_red = 0.0
     risk_red = 0.0;
     latency_red= 0.0;
     for j in range(trades.__len__()):
          if(count < green_number):
               count = count+1;
               profit_green = profit_green+trades[j][0];
               risk_green = risk_green+trades[j][1];
               latency_green = latency_green+trades[j][2];
          else:
               profit_red =profit_red + trades[j][0];
               risk_red = risk_red+trades[j][1];
               latency_red = latency_red+trades[j][2];

     profit_green = profit_green / green_number;
     risk_green = risk_green / green_number;
     latency_green = latency_green/ green_number;
     profit_red = profit_red/red_number;
     risk_red = risk_red/red_number;
     latency_red = latency_red/red_number;
     result = []
     for k in range(new_trades.__len__()):
          if(abs(new_trades[k][0] - profit_green) <(new_trades[k][0]-profit_red)):
               result.append("green");
          elif(abs(new_trades[k][0] - profit_green) >(new_trades[k][0]-profit_red)):
               result.append("red");
          else:
               if(abs(new_trades[k][0] - risk_green) <(new_trades[k][0]-risk_red)):
                    result.append("green");
               elif(abs(new_trades[k][0] - risk_green) >(new_trades[k][0]-risk_red)):
                    result.append("red");
               else:
                    if(abs(new_trades[k][0] - latency_green) <(new_trades[k][0]-latency_red)):
                         result.append("green");
                    else:
                         result.append("red");
     return result;