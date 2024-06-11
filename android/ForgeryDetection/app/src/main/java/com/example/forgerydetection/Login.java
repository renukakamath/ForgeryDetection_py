package com.example.forgerydetection;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

public class Login extends AppCompatActivity implements JsonResponse {

    EditText e1, e2, e3;
    Button b1, b2;
    public static String username, password, bbb, logid, usertype;
    SharedPreferences sh;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);
        sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());

        e1 = (EditText) findViewById(R.id.username);
        e2 = (EditText) findViewById(R.id.password);

        b1 = (Button) findViewById(R.id.loginbtn);
        b2 = (Button) findViewById(R.id.signup);

        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                username = e1.getText().toString();
                password = e2.getText().toString();
//                Toast.makeText(getApplicationContext(), ""+username+password,Toast.LENGTH_LONG).show();

                if (username.equalsIgnoreCase("")) {
                    e1.setError("Enter Your Username");
                    e1.setFocusable(true);
                } else if (password.equalsIgnoreCase("")) {
                    e2.setError("Enter Your Password");
                    e2.setFocusable(true);
                } else {

                        JsonReq JR = new JsonReq();
                        JR.json_response = (JsonResponse) Login.this;
                        String q = "/login?username="+username+"&password="+password;
                        q = q.replace(" ", "%20");
                        JR.execute(q);
                }
            }
        });
        b2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                startActivity(new Intent(getApplicationContext(), Reg.class));
            }
        });

    }

    @Override
    public void response(JSONObject jo) {
        try {
            String status = jo.getString("status");
            Log.d("pearl", status);

            if (status.equalsIgnoreCase("success")) {
                JSONArray ja1 = (JSONArray) jo.getJSONArray("data");
                logid = ja1.getJSONObject(0).getString("login_id");
                usertype = ja1.getJSONObject(0).getString("usertype");

                SharedPreferences.Editor e = sh.edit();
                e.putString("log_id", logid);
                e.commit();

                if (usertype.equals("user")) {
                    Toast.makeText(getApplicationContext(), "Login Successfully", Toast.LENGTH_SHORT).show();
                    startActivity(new Intent(getApplicationContext(), UserHome.class));}
                else if (usertype.equals("security authority")) {
                    Toast.makeText(getApplicationContext(), "Login Successfully", Toast.LENGTH_SHORT).show();
                    startActivity(new Intent(getApplicationContext(), SecurityHome.class));}
                else{
                        Toast.makeText(getApplicationContext(), "Login failed invalid username and password", Toast.LENGTH_LONG).show();
                        startActivity(new Intent(getApplicationContext(), Login.class));

                }
            }

        } catch (JSONException e) {

            Toast.makeText(getApplicationContext(), e.toString(), Toast.LENGTH_LONG).show();

        }

    }
    public void onBackPressed()
    {
        // TODO Auto-generated method stub
        super.onBackPressed();
        Intent b=new Intent(getApplicationContext(),IpSetting.class);
        startActivity(b);
    }
}