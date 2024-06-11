package com.example.forgerydetection;

import androidx.appcompat.app.AppCompatActivity;

import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.util.Log;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.Toast;

import org.json.JSONArray;
import org.json.JSONObject;

public class UserTravelHistory extends AppCompatActivity  implements JsonResponse{
    ListView l1;
    SharedPreferences sh;
    String[] fplace, tplace, date, value;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_user_travel_history);
        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        l1=(ListView) findViewById(R.id.lvhistory);

        JsonReq JR = new JsonReq();
        JR.json_response = (JsonResponse) UserTravelHistory.this;
        String q = "/travelhistory?lid="+sh.getString("log_id","");
        q = q.replace(" ", "%20");
        JR.execute(q);

    }

    @Override
    public void response(JSONObject jo) {
        try {

            String status = jo.getString("status");
            Log.d("pearl", status);

            if (status.equalsIgnoreCase("success")) {

                JSONArray ja1 = (JSONArray) jo.getJSONArray("data");
                fplace = new String[ja1.length()];
                tplace = new String[ja1.length()];
                date = new String[ja1.length()];
                value = new String[ja1.length()];

                for (int i = 0; i < ja1.length(); i++) {
                    fplace[i] = ja1.getJSONObject(i).getString("fplace");
                    tplace[i] = ja1.getJSONObject(i).getString("tplace");
                    date[i] = ja1.getJSONObject(i).getString("booked_for");

                    value[i] = "Travelled from , " + fplace[i] + " to  " + tplace[i] + " On  " + date[i]+"\n";
                }
                ArrayAdapter<String> ar = new ArrayAdapter<String>(getApplicationContext(), android.R.layout.simple_list_item_1, value);
                l1.setAdapter(ar);
            }
        }
        catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
            Toast.makeText(getApplicationContext(), e.toString(), Toast.LENGTH_LONG).show();
        }
    }
}