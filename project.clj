(defproject drum "0.1.0"
  :description "A sample project that used Clojure for REST API, OAUTH2 and dynamic generated documentation"
  :url "https://gitlab.com/condur/drum"
  :license {:name "Eclipse Public License"
            :url  "http://www.eclipse.org/legal/epl-v10.html"}
  :dependencies [[org.clojure/clojure "1.9.0-alpha9"]

                 [ring/ring-core "1.5.0"]
                 [ring/ring-jetty-adapter "1.5.0"]
                 [ring/ring-defaults "0.2.1"]
                 [ring/ring-json "0.4.0"]

                 [compojure "1.5.1"]

                 ]
  :main ^:skip-aot drum.core
  :target-path "target/%s"
  :profiles {:uberjar {:aot :all}
             :dev     {:plugins        []
                       :resource-paths ["resources"]
                       :dependencies   [[ring/ring-mock "0.3.0"]]}}
  :jvm-opts ["-server"])
