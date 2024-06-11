package com.example.forgerydetection;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.Toast;

import org.json.JSONArray;
import org.json.JSONObject;

public class UserEnquiry extends AppCompatActivity implements JsonResponse {
    SharedPreferences sh;
    String[] comp,rply,date,val;
    ListView l1;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_user_enquiry);

        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());

        l1 = findViewById(R.id.enqv);
        Button b1 = findViewById(R.id.btn);
        EditText e1 = findViewById(R.id.en);

        JsonReq JR = new JsonReq();
        JR.json_response = (JsonResponse) UserEnquiry.this;
        String q = "/viewenq?lid="+sh.getString("log_id","");
        q = q.replace(" ", "%20");
        JR.execute(q);

        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String enq = e1.getText().toString();

                if (enq.equalsIgnoreCase("")) {
                    e1.setError("Enter Enquiry details to Submit");
                    e1.setFocusable(true);
                }else {
                    JsonReq JR = new JsonReq();
                    JR.json_response = (JsonResponse) UserEnquiry.this;
                    String q = "/userenq?enq=" + enq + "&lid=" + sh.getString("log_id", "");
                    q = q.replace(" ", "%20");
                    JR.execute(q);
                }
            }
        });
    }

    @Override
    public void response(JSONObject jo) {
        try {



            String method = jo.getString("method");
            Log.d("result", method);
//                Toast.makeText(getApplicationContext(), status, Toast.LENGTH_LONG).show();

            if (method.equalsIgnoreCase("userenq")){
                String status = jo.getString("status");
                if (status.equalsIgnoreCase("success")) {


                    Toast.makeText(getApplicationContext(), "Enquiry Send Successfull", Toast.LENGTH_SHORT).show();
                    startActivity(new Intent(getApplicationContext(), UserEnquiry.class));
                    //startService(new Intent(getApplicationContext(),Notiservise.class));
                }
//

            }
             if (method.equalsIgnoreCase("viewenq")) {
                String status = jo.getString("status");
                Log.d("result", status);
                 if (status.equalsIgnoreCase("success")) {

                    JSONArray ja = (JSONArray) jo.getJSONArray("data");



                    comp = new String[ja.length()];
                    rply = new String[ja.length()];
                    date = new String[ja.length()];
                    val = new String[ja.length()];


                    for (int i = 0; i < ja.length(); i++) {


                        comp[i] = ja.getJSONObject(i).getString("enquiry");
                        rply[i] = ja.getJSONObject(i).getString("reply");
                        date[i] = ja.getJSONObject(i).getString("date");


                        val[i] = "Enquiry : " + comp[i]+"\nReply :" + rply[i] + "\nDate: " + date[i]+"\n";
                    }
                    l1.setAdapter(new ArrayAdapter<>(getApplicationContext(), android.R.layout.simple_list_item_1, val));

                }
            }





        } catch (Exception e) {
            e.printStackTrace();
            Toast.makeText(getApplicationContext(), e.toString(), Toast.LENGTH_LONG).show();
        }
    }
    public void onBackPressed()
    {
        // TODO Auto-generated method stub
        super.onBackPressed();
        Intent b=new Intent(getApplicationContext(),UserHome.class);
        startActivity(b);
    }
}